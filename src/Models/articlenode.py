import datetime
from src.Services.OpenAIIntegrations.OpenAIQueryService import OpenAIGetArticlePredecessors, OpenAIGetArticleSucessors
from src.Services.Webscraping.webscraper import parse, find_articles

class ArticleNode:

    def __init__(self, title: str, content: str, timestamp: datetime.datetime, link: str, depth: int, significance: int):
        self.title = title
        self.content = content
        self.timestamp = timestamp # datetime.datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%SZ")
        self.link = link
        self.predecessors = []
        self.successors = []
        self.depth = depth
        self.significance = significance

        print(self)

    def toJson(self):
        return {
            "title": self.title,
            "content": self.content,
            "publish_date": self.timestamp
        }

    def find_predecessors(self, num_preds=1):
        preds = OpenAIGetArticlePredecessors(self.toJson())


        if preds is None:
            return False

        preds.sort(key=lambda x: x[1], reverse=True)
        for i in range(min(num_preds, len(preds))):
            urls = find_articles(preds[i][0])

            if not urls:
                continue

            time_url = urls[min(1, len(urls) - 1)]
            title, content, publishDate = parse(time_url)
            if title is not None:
                article = ArticleNode(title, content, publishDate, time_url, 0, preds[i][1])
                article.successors.append(self)
                self.predecessors.append(article)
        
        return len(self.predecessors) > 0

    def find_sucessors(self, num_sucs=1):
        sucs = OpenAIGetArticleSucessors(self.toJson())
        if sucs is None:
            return False

        sucs.sort(key=lambda x: x[1], reverse=True)
        for i in range(min(num_sucs, len(sucs))):
            urls = find_articles(sucs[i][0])

            if not urls:
                continue

            time_url = urls[min(1, len(urls) - 1)]
            title, content, publishDate = parse(time_url)
            if title is not None:
                article = ArticleNode(title, content, publishDate, time_url, 0, sucs[i][1])
                article.predecessors.append(self)
                self.successors.append(article)
        
        return len(self.successors) > 0


    def __repr__(self):
        string = "\n--------------\n"
        string += f"Headline: {self.title}\n"
        string += f"Published: {self.timestamp}\n"
        string += f"Link: {self.link}\n"
        string += "\n--------------\n"

        return string