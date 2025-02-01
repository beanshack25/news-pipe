from src.Models.articlenode import ArticleNode
from src.Services.Webscraping.webscraper import parse, find_articles

def build_reg_tree(root: str):
    title, text, timestamp = parse(root)
    rootNode = ArticleNode(title, text, timestamp, root, 0, 0)

    # generate 2 generations of predecessors
    node = rootNode
    for i in range(2):

        print("Generating predecessors")

        if not node.find_predecessors(3):
            break
        node = node.predecessors[0]

    # try to generate 2 generations of sucessors
    node = rootNode
    for i in range(2):

        print("Generating sucessors")

        if not node.find_sucessors(2):
            break
        node = node.successors[0]

        


urln = "https://news.sky.com/story/teenage-gamer-becomes-first-person-to-beat-tetris-13041615"
build_reg_tree(urln)
