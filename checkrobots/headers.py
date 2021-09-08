"""
headers.py
Author: Niklas Larsson
Date: September 7, 2021
"""


def print_headers(headers: dict, sort: bool) -> None:
    """
    Print the request's headers for xtra info.
    
    Parameters
    ----------
    headers...... The request's headers in the format of dictionary.
    sort......... Alphabetically sort the header fields.
    """
    key: int = 0
    value: int = 1
    if (sort):
        for index, pair in enumerate(sorted(headers.items())):
            print("{}: {}".format(pair[key], pair[value]))
    else:
        for index, pair in enumerate(headers.items()):
            print("{}: {}".format(pair[key], pair[value]))
