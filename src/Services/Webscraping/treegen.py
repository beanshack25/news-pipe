from src.Models.articlenode import ArticleNode
from src.Services.OpenAIIntegrations.PredecessorService import query

def articleApiMethod(titleName: str) -> tuple[str, str, str, str]:
    return None, None, None, None


class Tree:
    def __init__(self, article: str, MAXD: int = 2):
        self.rootNode = None
        self.MAXD = MAXD
        self.build(article)

    def build(self, rootString):

        title, content, publishDate, url  = articleApiMethod(rootString)
        self.rootNode = ArticleNode(title, content, publishDate, url, 0, 10)

        q = [self.rootNode]

        while q:

            nodeOfInterest = q.pop(0)
            if nodeOfInterest.depth >= self.MAXD:
                continue

            results = query(nodeOfInterest)
            for pred in results["predecessors"]:
                title, content, publishDate, url = articleApiMethod(pred[0])
                article = ArticleNode(title, content, publishDate, url, nodeOfInterest.depth + 1, pred[1])
                q.append(article)
                nodeOfInterest.predecessors.append(article)