import unittest
from lib.get import get
from requests.exceptions import HTTPError, ConnectionError


def get_success(url):
    return "success"


def get_HTTPError(url):
    raise HTTPError()


def get_connectionerror(url):
    raise ConnectionError()


class TestGet(unittest.TestCase):

    def test_get(self):
        resp = get("", getUrl=get_success)
        self.assertEqual("success", resp)

    def test_get_httperror(self):
        with self.assertRaises(HTTPError):
            get("", getUrl=get_HTTPError)

    def test_get_connectionerror(self):
        with self.assertRaises(ConnectionError):
            get("", getUrl=get_connectionerror)
