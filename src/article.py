# Article class

# Stores list of topics, text content, sentiment, timeline, and other metadata of an article

import datetime

from sentiment import Sentiment

class Article:

    def __init__(self, text: str, topics: list[str], sentiment: Sentiment, timestamp: datetime.date):
        self.text = text
        self.topics = topics
        self.sentiment = sentiment
        self.timestamp = timestamp
    
