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
    # Create an instance of the schema for validation and consistent structure
    article_data = ArticleFrontMatter(
        title=title,
        link=link,
        summary=summary,
        tags=tags,
        published_date=published_date, # This will be aliased to 'date' in the output
        content_type=content_type,
        authors=authors,
        doi=doi
    )

    # Convert the Pydantic model to a dictionary, using aliases for keys
    # and excluding None values for cleaner YAML
    front_matter_dict = article_data.model_dump(by_alias=True, exclude_none=True)

    # Ensure date is formatted correctly for YAML
    if 'date' in front_matter_dict and isinstance(front_matter_dict['date'], datetime):
        front_matter_dict['date'] = front_matter_dict['date'].isoformat()

    # Use PyYAML to dump the dictionary to a YAML string
    yaml_front_matter = yaml.dump(front_matter_dict, sort_keys=False, default_flow_style=False, allow_unicode=True)

    # Construct the final Markdown content
    markdown_content = f"""---
{yaml_front_matter}---

"""

    return markdown_content

