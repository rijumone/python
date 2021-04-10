from loguru import logger
from flask import Flask, request

from shorturl.config import config
from shorturl.url_transform import URLTransform

logger.info('Initiating app.')
app = Flask(__name__)


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
        'data': f'{config["url_prefix"]}{short_url_suffix}',
    }, 200


@app.route('/decode')
def decode():
    request_json = request.get_json()
    short_url = request_json['short_url']

    # check if suffix exists here
    short_url_suffix = short_url.replace(f'{config["url_prefix"]}', '')

    url_transform = URLTransform()
    full_url = url_transform.decode(short_url_suffix)

    return {
        'message': 'success',
        'data': f'{full_url}'
    }, 200
