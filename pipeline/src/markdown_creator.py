from datetime import datetime
from content_classifier import ContentType
import json

def create_markdown_content(title: str, link: str, summary: str, tags: list[str], published_date: datetime, content_type: str, authors: list[str] = None, doi: str = None) -> str:
    """Generates a Markdown string with YAML front matter for a new article.

    Args:
        title: The title of the article.
        link: The URL of the original article.
        summary: The AI-generated summary of the article.
        tags: A list of AI-generated tags for the article.
        published_date: The publication date of the article.
        content_type: The type of the content (e.g., BLOG_POST).
        authors: Optional list of authors.
        doi: Optional DOI for research papers.

    Returns:
        A Markdown string with YAML front matter.
    """
    tags_yaml = ""
    if tags:
        formatted_tags = [f"  - {tag}" for tag in tags]
        tags_yaml = "\n" + "\n".join(formatted_tags)

    authors_yaml = ""
    if authors:
        formatted_authors = [f"  - {author}" for author in authors]
        authors_yaml = "\nauthors:\n" + "\n".join(formatted_authors)

    doi_yaml = f"\ndoi: \"{doi}\"" if doi else ""

    front_matter = f"""
---
title: "{title}"
date: {published_date.isoformat()}
link: "{link}"
summary: "{summary}"
tags:{tags_yaml}
categories:
  - {content_type}{authors_yaml}{doi_yaml}
---

"""

    return front_matter
