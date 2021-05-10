import json
import requests
from loguru import logger
url = 'https://jsonplaceholder.typicode.com/posts/{pg_num}'


def main():
    result = {}
    for pg_num in range(1, 11):
        result[pg_num] = {}
        try:
            final_url = url.format(pg_num=pg_num)
            logger.debug(final_url)

            response = requests.get(final_url)
            response_text = response.text
            logger.debug(response_text)
            try:
                response_json = response.json()
            except json.decoder.JSONDecodeError as _exc:
                logger.error(_exc)
                raise

            for item in ['title', 'body', ]:
                if item not in response_json:
                    logger.error(f'{item} not found in {response_text}')
                    raise KeyError

                _set = set()
                for word in response_json[item].split(' '):
                    _set.add(word)
                result[pg_num][item] = _set

        except KeyError:
            continue

    # check common words in both sets here
    common_words = set()

    for pg_num, data in result.items():
        for word in data['title']:
            if word in data['body']:
                # print(result[pg_num])
                common_words.add(word)

    return result, common_words


if __name__ == '__main__':
    result, common_words = main()
    logger.info(result)
    logger.info(common_words)


"""
Feedback:
- set intersect?
- how to make it more prod deployable
"""
