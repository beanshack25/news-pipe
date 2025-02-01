from src.Models.articlenode import ArticleNode
from src.Services.Webscraping.webscraper import parse, find_articles



def build_reg_tree(root: str, roots: list[ArticleNode]):
    title, text, timestamp = parse(root)
    rootNode = ArticleNode(title, text, timestamp, root, 0, 0)

    roots.append(rootNode)

    # generate 2 generations of predecessors
    node = rootNode
    for i in range(2):

        print("Generating predecessors")

        if not node.find_predecessors(3):
            break
        node = node.predecessors[0]

    # try to generate 2 generations of sucessors
    node = rootNode

    print("Generating sucessors")

    print(node.get_potential_future())

def explore_new_node(root: str, roots: list[ArticleNode]):
    title, text, timestamp = parse(root)
    rootNode = ArticleNode(title, text, timestamp, root, 0, 0)

    for node in roots:
        if node.includes(rootNode):
            node.explore_further(rootNode)
            break
    else:
        build_reg_tree(root, roots)
    
        
