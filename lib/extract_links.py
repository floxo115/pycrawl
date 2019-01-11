import re
from typing import List
from bs4 import Tag


def extract_links(html: Tag, pattern: str) -> List[str]:
    pattern = "^" + pattern + "$"
    links = html.find_all('a', {'href': re.compile(pattern, re.MULTILINE)})
    hrefs = []
    for link in links:
        if hasattr(link, 'attrs') and link.attrs.get('href'):
            hrefs.append(link.attrs['href'])
    return hrefs
