import sqlite3
import json
from pathlib import Path
from datetime import datetime
from database import get_db_connection

# Define the path for the output JSON file
ARTICLES_JSON_PATH = Path(__file__).parent.parent.parent / "site" / "data" / "articles.json"

def generate_articles_json():
    """Queries the published_content table and generates a JSON file for Hugo."""
    articles_data = []
    with get_db_connection() as conn:
        cursor = conn.execute("SELECT * FROM published_content ORDER BY published_date DESC")
        for row in cursor.fetchall():
            article = dict(row)
            # Convert datetime objects to ISO format strings for JSON
            if 'published_date' in article and isinstance(article['published_date'], datetime):
                article['published_date'] = article['published_date'].isoformat()
            # Parse JSON strings back to Python objects if needed (e.g., tags, authors)
            if 'tags' in article and article['tags']:
                article['tags'] = json.loads(article['tags'])
            if 'authors' in article and article['authors']:
                article['authors'] = json.loads(article['authors'])
            articles_data.append(article)

    # Ensure the output directory exists
    ARTICLES_JSON_PATH.parent.mkdir(parents=True, exist_ok=True)

    with open(ARTICLES_JSON_PATH, 'w') as f:
        json.dump(articles_data, f, indent=4)

    print(f"Generated {ARTICLES_JSON_PATH} with {len(articles_data)} articles.")
