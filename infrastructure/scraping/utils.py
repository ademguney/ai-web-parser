from bs4 import BeautifulSoup
from typing import List

def clean_html(html: str) -> str:
    """
    Cleans raw HTML content by removing script, style, and noscript tags,
    and returns plain cleaned text.
    """
    soup = BeautifulSoup(html, "html.parser")

    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()

    text = soup.get_text(separator="\n")
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    return "\n".join(lines)

def split_content(text: str, max_length: int = 6000) -> List[str]:
    """
    Splits long text into smaller chunks of maximum `max_length` characters.
    """
    return [text[i:i + max_length] for i in range(0, len(text), max_length)]