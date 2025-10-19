import feedparser
from datetime import datetime
from dateutil import parser

def fetch_articles(feed_urls: list[str], cut_off_date: datetime) -> list[dict]:
    """Fetches and filters articles from a list of RSS feeds.

    Args:
        feed_urls: A list of RSS feed URLs.
        cut_off_date: The cut-off date for filtering articles.

    Returns:
        A list of articles, where each article is a dictionary
        containing the title, link, and publication date.
    """
    articles = []
    for url in feed_urls:
        feed = feedparser.parse(url)
        for entry in feed.entries:
            published_date = parser.parse(entry['published'])
            if published_date.date() >= cut_off_date.date():
                articles.append({
                    'title': entry['title'],
                    'link': entry['link'],
                    'published': published_date,
                })
    return articles
