from datetime import datetime
from content_classifier import ContentType

def create_markdown_content(title: str, link: str, summary: str, tags: list[str], published_date: datetime, content_type: ContentType) -> str:
    """Generates a Markdown string with YAML front matter for a new article.

    Args:
        title: The title of the article.
        link: The URL of the original article.
        summary: The AI-generated summary of the article.
        tags: A list of AI-generated tags for the article.
        published_date: The publication date of the article.
        content_type: The type of the content (e.g., BLOG_POST).

    Returns:
        A Markdown string with YAML front matter.
    """
    tags_yaml = ""
    if tags:
        formatted_tags = [f"  - {tag}" for tag in tags]
        tags_yaml = "\n".join(formatted_tags)

    front_matter = f"""
---
title: "{title}"
date: {published_date.isoformat()}
link: "{link}"
summary: "{summary}"
tags:
{tags_yaml}
categories:
  - {content_type.value}
---

"

    return front_matter.format(title=title, published_date=published_date, link=link, summary=summary, tags_yaml=tags_yaml, content_type=content_type)