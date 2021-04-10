import os

from loguru import logger
from flask import Flask, request
from shorturl.url_transform import URLTransform


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'shortenurl.sqlite'),
        URL_PREFIX='https://short.est/',
    )
    # import pdb
    # pdb.set_trace()
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_json('config.json', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # print(app.config)
    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    @app.route('/encode')
    def encode():
        request_json = request.get_json()

        logger.debug(request_json)
        full_url = request_json['url']
        url_transform = URLTransform()
        short_url_suffix = url_transform.encode(
            full_url=full_url)

        return {
            'message': 'success',
            'data': f'{app.config["URL_PREFIX"]}{short_url_suffix}',
        }, 200

    @app.route('/decode')
    def decode():
        request_json = request.get_json()
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

    return app
