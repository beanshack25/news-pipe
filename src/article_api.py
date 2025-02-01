# from newsapi import NewsApiClient
import newsapi

import os

# run "export NEWS_API_KEY='your_key_here'" in terminal (and for ci will work automatically)

# Init
key = os.getenv('NEWS_API_KEY')
newsapi = newsapi.NewsApiClient(api_key=key)

# Given a query, return articles relevant to it
def getArticleFromApi(query):
  return newsapi.get_everything(q=query)['articles']