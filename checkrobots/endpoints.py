"""
headers.py
Author: Niklas Larsson
Date: September 7, 2021
"""


def count_allowed(response: object) -> int:
    """
    Get the amount of fields that start with 'Allow' from the response.
    """
    endpoints: int = 0
    for line in response.text.split("\n"):
        if (line.startswith("Allow")):
            endpoints += 1

    return endpoints


def count_disallowed(response: object) -> int:
    """
    Get the amount of fields that start with 'Disallow' from the response.
    """
    endpoints: int = 0
    for line in response.text.split("\n"):
        if (line.startswith("Disallow")):
            endpoints += 1

    return endpoints
