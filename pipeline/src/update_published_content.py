import sys
import os
import frontmatter
import sqlite3
from pathlib import Path
from datetime import datetime, timezone
import json
from pydantic import ValidationError

from database import get_db_connection, create_database
from article_schema import ArticleFrontMatter # Import the schema

ARTICLE_CONTENT_PATH = Path(__file__).parent.parent.parent / "site" / "content" / "posts"

def update_published_content_table(db_path=None):
    """Reads Markdown files from site/content/posts and updates the published_content table."""
    create_database(db_path) # Ensure database tables are created
    print(f"Scanning for Markdown files in: {ARTICLE_CONTENT_PATH}")
    for markdown_file in ARTICLE_CONTENT_PATH.glob("*.md"):
        try:
            with open(markdown_file, 'r') as f:
                post = frontmatter.load(f)
            print(f"DEBUG: Processing file: {markdown_file.name}")
            print(f"DEBUG: Front matter for {markdown_file.name}: {post.metadata}")
            
            # Validate front matter against the schema
            try:
                article_data = ArticleFrontMatter.model_validate(post.metadata)
            except ValidationError as e:
                print(f"Skipping {markdown_file.name}: Front matter validation failed: {e}")
                continue

            # Extract data from validated schema
            article_id = markdown_file.stem # Use filename as ID
            title = article_data.title
            url = article_data.link
            summary = article_data.summary
            source_name = post.metadata.get('source_name', 'Unknown') # source_name is not in schema, so get directly
            content_type = article_data.content_type
            publication_date = article_data.date
            authors = json.dumps(article_data.authors) if article_data.authors else None
            doi = article_data.doi
            tags = json.dumps(article_data.tags) if article_data.tags else None

            # Ensure publication_date is in UTC and naive for SQLite
            if publication_date.tzinfo is not None:
                publication_date = publication_date.astimezone(timezone.utc).replace(tzinfo=None)

            with get_db_connection(db_path) as conn:
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
    from database import DATABASE_PATH
    update_published_content_table(DATABASE_PATH)
