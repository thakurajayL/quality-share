import re
from enum import Enum
from urllib.parse import urlparse

class ContentType(Enum):
    BLOG_POST = "BLOG_POST"
    RESEARCH_PAPER = "RESEARCH_PAPER"
    ROOT_CAUSE_ANALYSIS = "ROOT_CAUSE_ANALYSIS"
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

    # Heuristic 3: Check for Root Cause Analysis keywords
    rca_keywords = ["postmortem", "root cause", "incident report", "failure analysis", "lessons learned"]
    if any(keyword in text_content.lower() for keyword in rca_keywords):
        return ContentType.ROOT_CAUSE_ANALYSIS

    # Default to BLOG_POST if no strong indicators for RESEARCH_PAPER or ROOT_CAUSE_ANALYSIS
    return ContentType.BLOG_POST
