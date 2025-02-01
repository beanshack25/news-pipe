from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='')

# Given a query, return articles relevant to it
def getArticleFromApi(query):
  return newsapi.get_everything(q=query)['articles']