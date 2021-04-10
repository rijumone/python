import os

from loguru import logger
from flask import Flask, request, abort
from flask_swagger_ui import get_swaggerui_blueprint
from werkzeug.exceptions import BadRequest
from shorturl.url_transform import URLTransform
from shorturl.validations import (EncodeInputSchema,
                                  DecodeInputSchema)


def setup_swagger_ui():
    # URL for exposing Swagger UI (without trailing '/')
    SWAGGER_URL = '/api/docs'

    # Our API url (can of course be a local resource)
    API_URL = 'http://petstore.swagger.io/v2/swagger.json'

    # Call factory function to create our blueprint
    swaggerui_blueprint = get_swaggerui_blueprint(
        # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
        SWAGGER_URL,
        API_URL,
        config={  # Swagger UI config overrides
            'app_name': "Test application"
        },
    )

    return swaggerui_blueprint


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
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

        request_json = request.get_json()
        validation_schema = EncodeInputSchema()
        errors = validation_schema.validate(request_json)
        if errors:
            return {
                'message': 'failure',
                'errors': errors,
            }, 400

        logger.debug(request_json)
        full_url = request_json['url']
        url_transform = URLTransform()
        short_url_suffix = url_transform.encode(
            full_url=full_url)

        return {
            'message': 'success',
            'data': f'{app.config["URL_PREFIX"]}{short_url_suffix}',
        }, 200

    @app.route('/decode', methods=['POST'])
    def decode():
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
        full_url = url_transform.decode(short_url_suffix)

        return {
            'message': 'success',
            'data': f'{full_url}'
        }, 200

    from . import db
    db.init_app(app)

    swaggerui_blueprint = setup_swagger_ui()

    app.register_blueprint(swaggerui_blueprint)

    return app
