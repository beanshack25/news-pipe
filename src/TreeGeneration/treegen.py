from src.Models.articlenode import ArticleNode
from src.Services.OpenAIIntegrations.PredecessorService import query
from src.Services.Webscraping.webscraper import parse, find_articles

class Tree:
    def __init__(self, articleURL: str, MAXD: int = 4):
        self.rootNode = None
        self.MAXD = MAXD
        self.build(articleURL)

    def build(self, rootString):

        title, content, publishDate  = parse(rootString)
        self.rootNode = ArticleNode(title, content, publishDate, rootString, 0, 10)

        q = [self.rootNode]

        while q:
            nodeOfInterest = q.pop(0)
            if nodeOfInterest.depth >= self.MAXD:
                continue

            results = query(nodeOfInterest)
            for pred in results["predecessors"]:
                urls = find_articles(pred[0])
                title, content, publishDate = parse(urls[1])
                article = ArticleNode(title, content, publishDate, urls[1], nodeOfInterest.depth + 1, pred[1])
                q.append(article)
                nodeOfInterest.predecessors.append(article)
                article.successors.append(nodeOfInterest)

    def __repr__(self):
        cns = [self.rootNode]
        string = ""
        while cns:
            cn = cns.pop(0)
            string += cn.title + "::" + str(cn.depth) + "\n----------------\n"
            cns.extend(cn.predecessors)

        return string


urln = "https://www.bbc.co.uk/news/articles/c98yn345555o"
tree = Tree(urln)
print(tree)
