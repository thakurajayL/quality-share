import re
from enum import Enum
from urllib.parse import urlparse

class ContentType(Enum):
    BLOG_POST = "BLOG_POST"
    RESEARCH_PAPER = "RESEARCH_PAPER"
    UNKNOWN = "UNKNOWN"

def classify_content(url: str, text_content: str) -> ContentType:
    """Classifies the content type based on URL and text heuristics.

    Args:
        url: The URL of the article.
        text_content: The extracted text content of the article.

    Returns:
        A ContentType enum value.
    """
    # Heuristic 1: Check URL for known research paper domains
    parsed_url = urlparse(url)
    if any(domain in parsed_url.netloc for domain in ["arxiv.org", "acm.org", "ieee.org", "springer.com", "sciencedirect.com"]):
        return ContentType.RESEARCH_PAPER

    # Heuristic 2: Check text content for DOI (Digital Object Identifier)
    if re.search(r'10\.\d{4,9}/[-._;()/:A-Z0-9]+', text_content, re.IGNORECASE):
        return ContentType.RESEARCH_PAPER

    # Default to BLOG_POST if no strong indicators for RESEARCH_PAPER
    return ContentType.BLOG_POST
