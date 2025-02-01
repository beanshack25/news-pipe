# Article class

# Stores list of topics, text content, sentiment, timeline, and other metadata of an article

class Article:

    def __init__(self, text, topics, sentiment, timeline, metadata):
        self.text = text
        self.topics = topics
        self.sentiment = sentiment
        self.timeline = timeline
        self.metadata = metadata
    
    