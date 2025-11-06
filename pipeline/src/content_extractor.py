import requests
import trafilatura
from io import BytesIO
from pypdf import PdfReader

def extract_content(url: str) -> str:
    """Extracts the main content from a URL, handling PDF files as well.

    Args:
        url: The URL of the article or PDF.

    Returns:
        The clean, main text of the content.
    """
    try:
        headers = {
            'User-Agent': 'quality-share-bot/1.0'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Raise an exception for bad status codes

        # Check if the content is a PDF
        if 'application/pdf' in response.headers.get('Content-Type', ''):
            with BytesIO(response.content) as f:
                reader = PdfReader(f)
                text = ""
                for page in reader.pages:
                    text += page.extract_text()
                return text
        else:
            # Use trafilatura to extract the main content from HTML
            content = trafilatura.extract(response.text)
            return content if content else ""
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL {url}: {e}")
        return ""
