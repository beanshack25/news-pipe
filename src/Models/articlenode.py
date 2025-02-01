import datetime

class ArticleNode:

    def __init__(self, title: str, content: str, timestamp: str, link: str, depth: int, significance: int):
        self.title = title
        self.content = content
        self.timestamp = datetime.datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%SZ")
        self.link = link
        self.predecessors = []
        self.depth = depth
        self.significance = significance

    def __repr__(self):
        string = ""
        string += f"Headline: {self.title}\n"
        string += f"Published: {self.timestamp}\n"
        string += f"Link: {self.link}\n"
        string += f"Text: \n{self.content}\n"

        return string