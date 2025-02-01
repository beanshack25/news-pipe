
from article import Article

from article_api import getArticleFromApi

class ArticlePipe:
    def __init__(self, article: Article):
        self.article = article
        self.children = []

        self.build_pipe()

    # Discover past and future articles to build a pipeline
    def build_pipe(self):
        
        query = self.article.headline
        timestamp = self.article.timestamp

        # Get other articles related to the query
        # print(query)
        articles = getArticleFromApi(query)
        print(articles)


    def add_child(self, child):
        self.children.append(child)

    def __call__(self):
        return self.article