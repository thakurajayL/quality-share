from datetime import datetime
from typing import List, Optional
import json
import yaml # Import yaml for proper YAML dumping

from article_schema import ArticleFrontMatter # Import the schema

def create_markdown_content(
    title: str,
    link: str,
    summary: str,
    tags: List[str],
    published_date: datetime,
    content_type: str,
    authors: Optional[List[str]] = None,
    doi: Optional[str] = None
) -> str:
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
    front_matter = [
        f"title: {title}",
        f"date: {published_date.isoformat()}",
        f"link: {link}",
        f"summary: {summary}",
    ]
    if tags:
        front_matter.append("tags:")
        front_matter.extend([f"- {tag}" for tag in tags])
    else:
        front_matter.append("tags: []")
    front_matter.append(f"content_type: {content_type}")
    if authors:
        front_matter.append("authors:")
        front_matter.extend([f"- {author}" for author in authors])
    if doi:
        front_matter.append(f"doi: {doi}")

    yaml_front_matter = "\n".join(front_matter)
    markdown_content = f"---\n{yaml_front_matter}\n---\n\n"
    return markdown_content