# from dataclasses import dataclass
import short_url
from loguru import logger

# from shorturl.database import DatabaseConnection
from shorturl.models import URLsMap
from shorturl.db import get_db_session
from shorturl.exceptions import ShortURL404


class ShortURL:
    # original_url: str
    @staticmethod
    def encode(unique_key):
        return short_url.encode_url(unique_key)

# @dataclass


class FullURL:
    # shorturl: str
    @staticmethod
    def decode(shorturl):
        return short_url.decode_url(shorturl)


class URLTransform:
    original_url = None

    def __init__(self) -> None:
        # self.db_session = DatabaseConnection().get_db_session()
        self.db_session = get_db_session()

    def encode(self, original_url):
        self.original_url = original_url

        # generate unique integer
        unique_integer = self.db_insert()

        # generate unique short url
        self.short_url_suffix = ShortURL.encode(
            unique_key=unique_integer)

        # persist to generated short url to storage
        self.db_update()
        logger.debug(self.short_url_suffix)

        return self.short_url_suffix

    def db_insert(self, ):
        self.db_url = URLsMap()
        self.db_url.original_url = self.original_url
        self.db_session.add(self.db_url)
        self.db_session.commit()
        logger.debug(self.db_url.id)
        return self.db_url.id

    def db_update(self, ):
        self.db_url.short_url = self.short_url_suffix
        self.db_session.add(self.db_url)
        self.db_session.commit()

    def decode(self, short_url_suffix):
        self.short_url_suffix = short_url_suffix

        # reverse generate the unique integer
        # used to create the suffix
        try:
            url_id = FullURL.decode(self.short_url_suffix)
        except ValueError:
            logger.error(
                f'Unable to decode short_url: {self.short_url_suffix}.')
            raise ShortURL404('Unable to decode short_url: {short_url}')

        # fetch the db_url object from db
        self.db_url = self.db_session.query(URLsMap).get(url_id)
        if not self.db_url:
            logger.error(
                f'short_url: {self.short_url_suffix} does not exist.')
            raise ShortURL404('{short_url} does not exist')

        # logger.debug(self.db_url)
        logger.debug(self.db_url.original_url)

        return self.db_url.original_url


if __name__ == '__main__':

    url_transform = URLTransform()
    short_url_suffix = url_transform.encode(
        original_url='https://codesubmit.io/library/react')

    url_transform.decode(short_url_suffix)
