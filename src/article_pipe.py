
from article import Article

class ArticlePipe:
    def __init__(self, article: Article):
        self.article = article
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def __call__(self):
        return self.article