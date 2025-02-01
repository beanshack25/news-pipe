from typing import Any
from src.Models.articlenode import ArticleNode

def ArticleToJsonAdapter(article: ArticleNode) -> dict[str, Any]:
    return {
        "title": article.title,
        "content": article.content,
        "publish_date": article.timestamp
    }