import requests
from bs4 import BeautifulSoup
from newspaper import Article as NewsArticle
import time
import os

url_base = r"https://www.news.google.com/"
url_search = url_base + r"search?q="

seid = "65b91f9076f514217"
seapi = os.environ.get("SEAPI_KEY")

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}

def getTimeStamp(title):
    url = url_search + title.replace(" ", "+")
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

def make_datetime_month_year(time):
    time = time.split("T")[0].split("-")
    time = time[1] + "-" + time[0]
    return time

def find_volume_articles(soup):

    time_volume = {}

    for article in soup.find_all("time", {"class": "hvbAAd"}):
        # Get the month of publish
        time = make_datetime_month_year(article["datetime"])

        if time in time_volume:
            time_volume[time] += 1
        else:
            time_volume[time] = 1

    return time_volume


def find_articles(topic):
    url = url_search + topic.replace(" ", "+")
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    time_volume = find_volume_articles(soup)

    event_time = max(time_volume, key=time_volume.get)

    articles = soup.find_all("article")

    ret_articles = [articles[0]]

    for article in articles:
        if make_datetime_month_year(article.find("time", {"class": "hvbAAd"})["datetime"]) == event_time:
            if article not in ret_articles:
                ret_articles.append(article)
                break

    ret = []
    for article in ret_articles:

        title = article.find("button")["aria-label"].split(" - ")[1].replace(" ", "+")

        url = f'https://www.googleapis.com/customsearch/v1?q={title}&cx={seid}&key={seapi}'

        response = requests.get(url)
        data = response.json()

        for item in data["items"]:
            if "news" in item["link"]:
                url = item["link"]
                break

        ret.append(url)


    return ret