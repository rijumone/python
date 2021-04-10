import os

from loguru import logger
from flask import Flask, request, abort
from flasgger import Swagger
from shorturl.url_transform import URLTransform
from shorturl.exceptions import ShortURL404
from shorturl.validations import (EncodeInputSchema,
                                  DecodeInputSchema)


def create_app(test_config=None):
    """
    Flask app factory.
    Loads configs.
    Sets up logging.
    Defines routes.
    Initializes app.

    Args:
        test_config: test config to be passed while running tests

    Returns:
        Flask app
    """
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    swagger = Swagger(app)

    app.config.from_mapping(
        DATABASE=os.path.join(app.instance_path, 'shortenurl.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_json('config.json', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/encode', methods=['POST'])
    def encode():
        """Encodes a URL to shortened URL.
        Returns a short URL
        ---
        consumes:
          - application/json
        produces:
          - application/json
        parameters:
          - name: url
            in: body
            required: true
            description: The URL to shorten.
            schema:
              type: object
              required:
                - url
              properties:
                url:
                  type: string
        definitions:
          ShortURLSuccess:
            type: object
            properties:
              data:
                type: string
              message:
                type: string
          ShortURLFailure:
            type: object
            properties:
              message:
                type: string
              errors:
                type: string
        responses:
          200:
            description: A JSON object containing the shortened URL.
            schema:
              $ref: '#/definitions/ShortURLSuccess'
          400:
            description: A JSON object containing validation errors.
            schema:
              $ref: '#/definitions/ShortURLFailure'

        """

        request_json = request.get_json()
        validation_schema = EncodeInputSchema()
        errors = validation_schema.validate(request_json)
        if errors:
            return {
                'message': 'failure',
                'errors': errors,
            }, 400

        logger.debug(request_json)
        original_url = request_json['url']
        url_transform = URLTransform()
        short_url_suffix = url_transform.encode(
            original_url=original_url)

        return {
            'message': 'success',
            'data': f'{app.config["URL_PREFIX"]}{short_url_suffix}',
        }, 200

    @app.route('/decode', methods=['POST'])
    def decode():
        """Decodes a short URL to the original URL.
        Returns the original URL.
        ---
        consumes:
          - application/json
        produces:
          - application/json
        parameters:
          - name: short_url
            in: body
            required: true
            description: The short URL to decode.
            schema:
              type: object
              required:
                - short_url
              properties:
                short_url:
                  type: string
        definitions:
          URLSuccess:
            type: object
            properties:
              data:
                type: string
              message:
                type: string
          URLFailure:
            type: object
            properties:
              message:
                type: string
              errors:
                type: string
        responses:
          200:
            description: A JSON object containing the shortened URL.
            schema:
              $ref: '#/definitions/URLSuccess'
          400:
            description: A JSON object containing validation errors.
            schema:
              $ref: '#/definitions/URLFailure'
          404:
            description: A JSON object containing decoding errors.
            schema:
              $ref: '#/definitions/URLFailure'

        """
        request_json = request.get_json()
        validation_schema = DecodeInputSchema()
        errors = validation_schema.validate(request_json)
        if errors:
            return {
                'message': 'failure',
                'errors': errors,
            }, 400
        short_url = request_json['short_url']

        # check if suffix exists here
        short_url_suffix = short_url.replace(f'{app.config["URL_PREFIX"]}', '')

        url_transform = URLTransform()
        try:
            original_url = url_transform.decode(short_url_suffix)
        except ShortURL404 as exc404:
            return {
                'message': 'failure',
                'errors': f'{exc404}'.format(short_url=short_url)
            }, 404

        return {
            'message': 'success',
            'data': f'{original_url}'
        }, 200

    from . import db
    db.init_app(app)

    return app
