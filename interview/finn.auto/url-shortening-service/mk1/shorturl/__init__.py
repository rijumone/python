import os

from loguru import logger
from flask import Flask, request
from flasgger import Swagger
from shorturl.url_transform import URLTransform
from shorturl.exceptions import ShortURL404
from shorturl.blueprints import shorturl_bp
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

    from . import db
    db.init_app(app)

    app.register_blueprint(shorturl_bp)

    return app
