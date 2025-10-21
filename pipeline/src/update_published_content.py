import sys
import os
import frontmatter
import sqlite3
from pathlib import Path
from datetime import datetime, timezone
import json

from database import get_db_connection

ARTICLE_CONTENT_PATH = Path(__file__).parent.parent.parent / "site" / "content" / "posts"

def update_published_content_table():
    """Reads Markdown files from site/content/posts and updates the published_content table."""
    print(f"Scanning for Markdown files in: {ARTICLE_CONTENT_PATH}")
    for markdown_file in ARTICLE_CONTENT_PATH.glob("*.md"):
        try:
            with open(markdown_file, 'r') as f:
                post = frontmatter.load(f)
            
            # Extract data from front matter
            article_id = post.metadata.get('id', markdown_file.stem) # Use filename as ID if not present
            title = post.metadata.get('title')
            url = post.metadata.get('link')
            summary = post.metadata.get('summary')
            source_name = post.metadata.get('source_name', 'Unknown')
            content_type = post.metadata.get('content_type')
            publication_date_str = post.metadata.get('published_date')

            authors_data = post.metadata.get('authors', [])
            if isinstance(authors_data, str):
                authors_data = [authors_data]
            authors = json.dumps(authors_data)
            doi = post.metadata.get('doi', '')
            tags_data = post.metadata.get('tags', [])
            if isinstance(tags_data, str):
                tags_data = [tags_data]
            tags = json.dumps(tags_data)

            if not all([title, url, content_type, publication_date_str]):
                print(f"Skipping {markdown_file.name}: Missing required front matter fields.")
                continue

            # Convert publication_date to datetime object and make it timezone-naive
            publication_date = datetime.fromisoformat(publication_date_str.replace('Z', '+00:00'))
            if publication_date.tzinfo is not None:
                publication_date = publication_date.astimezone(timezone.utc).replace(tzinfo=None)

            with get_db_connection() as conn:
                # Check if article already exists to prevent duplicates
                cursor = conn.execute("SELECT id FROM published_content WHERE url = ?", (url,))
                if cursor.fetchone():
                    print(f"Article {title} (URL: {url}) already exists in published_content. Skipping.")
                    continue

                conn.execute("""
                    INSERT INTO published_content (id, title, url, summary, source_name, content_type, publication_date, authors, doi, tags)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    article_id,
                    title,
                    url,
                    summary,
                    source_name,
                    content_type,
                    publication_date,
                    authors,
                    doi,
                    tags
                ))
                conn.commit()
                print(f"Added {title} to published_content table.")

        except Exception as e:
            print(f"Error processing {markdown_file.name}: {e}")
            import traceback
            traceback.print_exc()
            sys.exit(1)

if __name__ == "__main__":
    update_published_content_table()

if __name__ == "__main__":
    update_published_content_table()
