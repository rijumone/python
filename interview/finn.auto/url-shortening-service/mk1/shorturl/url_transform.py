# from dataclasses import dataclass
import short_url
from loguru import logger

# from shorturl.database import DatabaseConnection
from shorturl.models import URLsMap
from shorturl.db import get_db, get_db_session

# @dataclass


class ShortURL:
    # full_url: str
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
    full_url = None

    def __init__(self) -> None:
        # self.db_session = DatabaseConnection().get_db_session()
        self.db_session = get_db_session()

    def encode(self, full_url):
        self.full_url = full_url

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
        self.db_url.full_url = self.full_url
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
        url_id = FullURL.decode(self.short_url_suffix)

        # fetch the db_url object from db
        self.db_url = self.db_session.query(URLsMap).get(url_id)

        # self.db_url = self.db.query(URLsMap).get(url_id)

        # logger.debug(self.db_url)
        logger.debug(self.db_url.full_url)

        return self.db_url.full_url


if __name__ == '__main__':

    url_transform = URLTransform()
    short_url_suffix = url_transform.encode(
        full_url='https://codesubmit.io/library/react')

    url_transform.decode(short_url_suffix)
