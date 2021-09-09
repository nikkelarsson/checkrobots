"""
robots.py – Print contents of the robots.txt.
Author: Niklas Larsson
Date: September 7, 2021
"""


def print_allowed(robots_txt: str, sort: bool) -> None:
    """
    Print fields from the robots.txt that begin with 'Allow'.

    Parameters
    ----------
    robots_txt......... Robots.txt in plain/text -format.
    sort............... Alphabetically sort the endpoints.
    """
    endpoints: list = []
    min_valid_len: int = len("Allow:")
    for line in robots_txt.split("\n"):
        if (line.startswith("Allow")):
            if (len(line) > min_valid_len):
                endpoints.append(line.replace("Allow: ", ""))
    if (sort):
        for index, line in enumerate(sorted(endpoints), 1):
            print("{}) {}".format(index, line.strip()))
    else:
        for index, line in enumerate(endpoints, 1):
            print("{}) {}".format(index, line.strip()))


def print_disallowed(robots_txt: str, sort: bool) -> None:
    """
    Print fields from the robots.txt that begin with 'Disallow'.

    Parameters
    ----------
    robots_txt......... Robots.txt in plain/text -format.
    sort............... Alphabetically sort the endpoints.
    """
    endpoints: list = []
    min_valid_len: int = len("Disallow:")
    for line in robots_txt.split("\n"):
        if (line.startswith("Disallow")):
            if (len(line) > min_valid_len):
                endpoints.append(line.replace("Disallow: ", ""))
    if (sort):
        for index, line in enumerate(sorted(endpoints), 1):
            print("Endpoint [{}] --> {}".format(index, line.strip()))
    else:
        for index, line in enumerate(endpoints, 1):
            print("Endpoint [{}] --> {}".format(index, line.strip()))


def print_raw(robots_txt: str) -> None:
    """
    Print site's robots.txt "as is".

    Parameters
    ----------
    robots_txt...... Contents of the robots.txt in plain/text format.
    """
    for line in robots_txt.split("\n"):
        print(line)
