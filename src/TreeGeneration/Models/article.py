# Article class

# Stores list of topics, text content, sentiment, timeline, and other metadata of an article

import datetime

from sentiment import Sentiment

class Article:

    def __init__(self, text: str, topics: list[str], sentiment: Sentiment, timestamp: datetime.date, link: str, headline: str):
        self.text = text
        self.topics = topics
        self.sentiment = sentiment
        self.timestamp = timestamp
        self.link = link
        self.headline = headline

    def __repr__(self):
        string = ""
        string += f"Headline: {self.headline}\n"
        string += f"Published: {self.timestamp}\n"
        string += f"Link: {self.link}\n"
        string += f"Text: \n{self.text}\n"

        return string
    
