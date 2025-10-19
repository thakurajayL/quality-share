import requests
import trafilatura

def extract_content(url: str) -> str:
    """Extracts the main content from a URL.

    Args:
        url: The URL of the article.

    Returns:
        The clean, main text of the article.
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status() # Raise an exception for bad status codes
        # Use trafilatura to extract the main content
        content = trafilatura.extract(response.text)
        return content if content else ""
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL {url}: {e}")
        return ""
