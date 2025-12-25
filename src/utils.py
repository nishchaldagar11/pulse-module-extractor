from urllib.parse import urlparse


def is_valid_url(url):
    """
    Validate if input is a proper URL
    """
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except Exception:
        return False


def normalize_title(title):
    """
    Normalize headings to avoid duplicate modules
    Example:
    'Account settings ' -> 'Account Settings'
    """
    if not title:
        return ""

    title = title.strip().lower()
    return title.title()


def truncate_text(text, max_length=250):
    """
    Safely truncate text without breaking words
    """
    if not text:
        return ""

    if len(text) <= max_length:
        return text

    return text[:max_length].rsplit(" ", 1)[0] + "..."
