import pytest
from infrastructure.scraping.utils import clean_html, split_content

def test_clean_html_removes_unwanted_tags():
    raw_html = """
        <html>
            <head>
                <style>body { color: red; }</style>
                <script>alert("hello");</script>
                <noscript>Javascript is disabled</noscript>
            </head>
            <body>
                <h1>Başlık</h1>
                <p>İçerik burada.</p>
            </body>
        </html>
    """
    cleaned = clean_html(raw_html)
    assert "alert" not in cleaned
    assert "color: red" not in cleaned
    assert "Javascript is disabled" not in cleaned
    assert "Başlık" in cleaned
    assert "İçerik burada." in cleaned

def test_clean_html_removes_blank_lines():
    raw_html = "<p>Line 1</p>\n<p>  </p>\n<p>Line 2</p>"
    cleaned = clean_html(raw_html)
    lines = cleaned.splitlines()
    assert lines == ["Line 1", "Line 2"]

def test_split_content_splits_long_text_correctly():
    text = "abcde" * 3000 
    chunks = split_content(text, max_length=6000)
    assert len(chunks) == 3
    assert all(len(chunk) <= 6000 for chunk in chunks)
    assert "".join(chunks) == text  