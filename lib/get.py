import logging
import time
import requests
from requests.exceptions import HTTPError, ConnectionError


def get(url,
        max_tries=3,
        sleep_seconds=1,
        getUrl=requests.get) -> requests.Response:
    """ get simply sends a GET request to a URL and returns the response """
    num_tries = 1

    while True:
        try:
            return getUrl(url)
        except (HTTPError, ConnectionError):
            logging.error(f"while getting {url}")

            num_tries += 1
            if num_tries == max_tries:
                raise

            time.sleep(sleep_seconds)
