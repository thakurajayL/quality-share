from datetime import datetime

def create_markdown_content(title: str, link: str, summary: str, tags: list[str], published_date: datetime) -> str:
    """Generates a Markdown string with YAML front matter for a new article.

    Args:
        title: The title of the article.
        link: The URL of the original article.
        summary: The AI-generated summary of the article.
        tags: A list of AI-generated tags for the article.
        published_date: The publication date of the article.

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
---

"""

    return front_matter.format(title=title, published_date=published_date, link=link, summary=summary, tags_yaml=tags_yaml)
