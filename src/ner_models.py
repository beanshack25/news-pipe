from webstruct.model import CRFTagger
from webstruct.html import tokenize_html

import requests
from bs4 import BeautifulSoup

html = requests.get("https://www.bbc.co.uk/news/live/cn4z119e5xxt").text
tokens = list(tokenize_html(html))
tagger = CRFTagger()

train_data = [

    ("title", "BTITLE")

]