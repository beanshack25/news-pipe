from article_pipe import ArticlePipe
from article import Article
from sentiment import Sentiment
from datetime import datetime


a = Article(
    "test html",
    ["test", "html"],
    Sentiment.POSITIVE,
    datetime.now(),
    r"https://www.bbc.co.uk/news/live/cn4z119e5xxt",
    "israeli hostage"
)

pipe = ArticlePipe(a)

