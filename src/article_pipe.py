
from article import Article

class ArticlePipe:
    def __init__(self, article: Article):
        self.article = article
        self.children = []

    def __call__(self):
        return self.article