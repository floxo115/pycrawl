import unittest

from bs4 import BeautifulSoup

from lib.extract_links import extract_links

input = """
<html>
<body>
<a href="http://www.google.de">google</a>
<a href="http://www.gmx.de">google</a>
<a href="http://www.standard.at">google</a>
<div>
<a href="http://www.amazon.de">google</a>
</div>
<a href="/static/img/img.png">google</a>
</body>
</html>
"""


class TextExtractLinks(unittest.TestCase):
    def test_extract_links(self):
        html = BeautifulSoup(input, 'html.parser')

        links = extract_links(html, "http://.*")
        expected = [
            "http://www.google.de",
            "http://www.gmx.de",
            "http://www.standard.at",
            "http://www.amazon.de",
        ]
        self.assertEqual(expected, links)

        links = extract_links(html, "/.*")
        print(links)
        expected = ["/static/img/img.png"]
        self.assertEqual(expected, links)
