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
    for line in robots_txt.split("\n"):
        if (line.startswith("Allow")):
            endpoints.append(line.replace("Allow: ", ""))
    if (sort):
        for index, line in enumerate(sorted(endpoints), 1):
            print("Endpoint [{}] --> {}".format(index, line.strip()))
    else:
        for index, line in enumerate(endpoints, 1):
            print("Endpoint [{}] --> {}".format(index, line.strip()))


def print_disallowed(robots_txt: str, sort: bool) -> None:
    """
    Print fields from the robots.txt that begin with 'Disallow'.

    Parameters
    ----------
    robots_txt......... Robots.txt in plain/text -format.
    sort............... Alphabetically sort the endpoints.
    """
    endpoints: list = []
    for line in robots_txt.split("\n"):
        if (line.startswith("Disallow")):
            endpoints.append(line.replace("Disallow: ", ""))
    if (sort):
        for index, line in enumerate(sorted(endpoints), 1):
            print("Endpoint [{}] --> {}".format(index, line.strip()))
    else:
        for index, line in enumerate(endpoints, 1):
            print("Endpoint [{}] --> {}".format(index, line.strip()))
