import sqlite3
import json
from pathlib import Path
from datetime import datetime
from database import get_db_connection
from markdown_creator import create_markdown_content
import re

# Define the path for the output JSON file
ARTICLES_JSON_PATH = Path(__file__).parent.parent.parent / "site" / "data" / "articles.json"
ARTICLE_CONTENT_PATH = Path(__file__).parent.parent.parent / "site" / "content" / "posts"

def slugify(text):
    text = re.sub(r'\s+', '-', text)  # Replace spaces with hyphens
    text = re.sub(r'[^a-zA-Z0-9-]', '', text)  # Remove non-alphanumeric characters except hyphens
    return text.lower()

def generate_articles_json_and_markdown():
    """Queries the published_content table and generates a JSON file for Hugo and individual Markdown files."""
    articles_data = []
    ARTICLE_CONTENT_PATH.mkdir(parents=True, exist_ok=True)

    with get_db_connection() as conn:
        cursor = conn.execute("SELECT * FROM published_content ORDER BY publication_date DESC")
        for row in cursor.fetchall():
            article = dict(row)
            
            # Convert datetime objects to ISO format strings for JSON
            if 'publication_date' in article and isinstance(article['publication_date'], datetime):
                article['publication_date'] = article['publication_date'].isoformat()
            
            # Parse JSON strings back to Python objects if needed (e.g., tags, authors)
            if 'tags' in article and article['tags']:
                article['tags'] = json.loads(article['tags'])
            else:
                article['tags'] = []
            
            if 'authors' in article and article['authors']:
                article['authors'] = json.loads(article['authors'])
            else:
                article['authors'] = []

            # Transform the article data to the desired JSON structure
            transformed_article = {
                "title": article["title"],
                "link": article["url"],
                "summary": article["summary"],
                "tags": article["tags"],
                "date": datetime.fromisoformat(article["publication_date"]).isoformat(),
                "content_type": article["content_type"],
                "authors": article["authors"],
                "doi": article.get("doi")
            }
            articles_data.append(transformed_article)

            # Create individual Markdown file
            file_name = slugify(article['title']) + ".md"
            file_path = ARTICLE_CONTENT_PATH / file_name

            markdown_content = create_markdown_content(
                title=article['title'],
                link=article['url'],
                summary=article['summary'],
                tags=article['tags'],
                published_date=datetime.fromisoformat(article['publication_date']),
                content_type=article['content_type'],
                authors=article.get('authors'), # Safely get authors
                doi=article.get('doi') # Safely get doi
            )

            with open(file_path, 'w') as f:
                f.write(markdown_content)
            print(f"Generated Markdown for {article['title']} at {file_path}")

    # Ensure the output directory for JSON exists
    ARTICLES_JSON_PATH.parent.mkdir(parents=True, exist_ok=True)

    with open(ARTICLES_JSON_PATH, 'w') as f:
        json.dump(articles_data, f, indent=4)

    print(f"Generated {ARTICLES_JSON_PATH} with {len(articles_data)} articles.")
