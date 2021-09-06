"""
urls.py – List of websites to fetch robots.txt from.
Author: Niklas Larsson
Date: 5.9.2021
"""


# Website names with their corresponding urls to the robots.txt.
WEBSITES: dict = {
        "youtube": "https://www.youtube.com/robots.txt",
        "google": "https://www.google.fi/robots.txt",
        "chess": "https://www.chess.com/robots.txt"
        }

def gen_url(website: str) -> str:
    """
    Generate a url by looking at the website's name.

    Parameters
    ----------
    website...... Website's name (google, youtube etc).
    """
    url: str = ""
    for i in WEBSITES.items():
        if (website == i[0]):
            url = i[1]
            break

    return url
