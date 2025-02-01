from newspaper import Article

# Define the article URL
url = "https://www.bbc.co.uk/news/live/cn4z119e5xxt"  # Replace with any news article URL

# Create an Article object
article = Article(url)

# Download and parse the article
article.download()
article.parse()

# Print extracted information
print("Title:", article.title)
print("Publication Date:", article.publish_date)
print("\nArticle Text:\n", article.text)