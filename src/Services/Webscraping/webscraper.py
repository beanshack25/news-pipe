import requests
from bs4 import BeautifulSoup
from newspaper import Article as NewsArticle

def getTimeStamp(title):
    url_base = r"https://www.news.google.com/search?q="
    url = url_base + title.replace(" ", "+")
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    time = soup.find("time", {"class": "hvbAAd"})
    return time["datetime"]

def parse(url):

    article = NewsArticle(url)
    article.download()
    article.parse()

    title = article.title
    text = article.text

    timestamp = article.publish_date
    if timestamp is None:
        timestamp = getTimeStamp(title)

    return title, text, timestamp
