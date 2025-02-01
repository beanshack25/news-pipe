# Scrape news articles from the web

import requests
from bs4 import BeautifulSoup

def get_news_articles(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Failed to fetch the page, status code: {response.status_code}")
        return None

    soup = BeautifulSoup(response.text, "html.parser")

    print(soup.find("meta", {"property": "article:published_time"}) or soup.find("meta", {"name": "date"}))

    # Extract the article headline
    headline = soup.find("h1").get_text(strip=True) if soup.find("h1") else "No headline found"

    # Extract the publish date (if available)
    time_tag = soup.find("time")
    publish_date = time_tag["datetime"] if time_tag and "datetime" in time_tag.attrs else "No date found"

    # Extract the article body
    paragraphs = soup.find_all("p")
    content = "\n".join(p.get_text(strip=True) for p in paragraphs)

    return {"headline": headline, "content": content, "publish_date": publish_date}
