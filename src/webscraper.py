# Scrape news articles from the web

import requests
from bs4 import BeautifulSoup

def get_news_articles(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    articles = soup.find_all('article')
    output = []
    for article in articles:
        title = article.h2.a.text
        body = article.find('div', class_='entry-content').p.text
        output.append({'title': title, 'body': body})
    return output