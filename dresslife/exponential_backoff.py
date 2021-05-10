from time import sleep

import requests
from loguru import logger

url = 'http://httpstat.us/500'
MAX_RETRIES = 3
INIT_SLEEP_SECONDS = 1
SLEEP_SECONDS_MULTIPLIER = 2


def main():
    retry_ctr = 0
    sleep_seconds = INIT_SLEEP_SECONDS * SLEEP_SECONDS_MULTIPLIER
    while retry_ctr < MAX_RETRIES:
        try:
            response = requests.get(url)
            # logger.info(response.status_code)
            if response.status_code >= 500:
                raise requests.exceptions.RequestException
            logger.info(response.text)
            break
        except requests.exceptions.RequestException as _exc:
            logger.warning(_exc)
            retry_ctr += 1

            logger.info(f'sleeping for {sleep_seconds} second(s).')
            sleep_seconds *= SLEEP_SECONDS_MULTIPLIER
            sleep(sleep_seconds)
            continue

    if retry_ctr == MAX_RETRIES:
        logger.critical(
            f'Loading URL: {url} failed after max retries: {MAX_RETRIES}')


if __name__ == '__main__':
    main()

"""
Feedback:
- how is it a module?
- the exceptions caught, when will they be raised?
"""
