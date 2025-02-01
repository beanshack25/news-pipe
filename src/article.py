# Article class

# Stores list of topics, text content, sentiment, timeline, and other metadata of an article

import datetime

class Article:

    def __init__(self, text: str, topics: list[str], sentiment, timestamp: datetime.date):
        self.text = text
        self.topics = topics
        self.sentiment = sentiment
        self.timestamp = timestamp
    
