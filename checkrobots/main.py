"""
main.py – Web 'spider' that checks sites, and if they allow webscraping.
Author: Niklas Larsson
Date: 29.8.2021
"""

import requests
import sys


def print_headers(headers: dict, limit=None, sort: bool=True) -> None:
    """
    Print the request's headers for xtra info.
    
    Parameters
    ----------
    headers...... The request's headers in the format of dictionary.
    limit........ The limit how many header fields to print.
    sort......... Alphabetically sort the header fields.
    """
    key: int = 0; value: int = 1
    print("----- HEADERS -----")
    for index, pair in enumerate(sorted(headers.items()) if (sort) else headers.items()):
        if (limit is not None) and (index == limit):
            break
        print("{}: {}".format(pair[key], pair[value]))
    print()


def print_robots(robots: str, sort: bool=True) -> None:
    """
    Print request's robots.txt's contents.

    Parameters
    ----------
    robots....... The actual robots.txt content in plain/text.
    sort......... Alphabetically sort the 'rool' fields.
    """
    scraping_not_suitable: bool = "Allow" not in robots
    print("----- ROBOTS.TXT -----")
    if (scraping_not_suitable):
        print("PLEASE NOTE, THAT WE DON'T ALLOW SCRAPING THIS SITE.")
    else:
        print(robots)


def get_response(url: str, bar: bool) -> object:
    """
    Fetch the response object, A.K.A the robots.txt.

    Parameters
    ----------
    url........ Get the robots.txt of this url.
    bar........ Print an indicator of sorts to indicate something's happening.
    """
    try:
        if (bar):
            print("Trying to fetch robots.txt ...")
            print("[Address]: {}".format(url))
        response: object = requests.get(url)
        print() if (bar) else print(end="")
    except requests.ConnectionError as exception:
        sys.exit("{}: Error: Couldn't connect to {} ...".format(sys.argv[0], url))
    
    return response


def print_all(url: str, verbose: bool, headers: bool) -> None:
    """
    Print out all: the actual robots.txt, and additionally headers.
    
    Parameters
    ----------
    url.......... Use this url to fetch the robots.txt.
    verbose...... Let the output be a little more verbose.
    headers...... Also print the headers in addition to the robots.txt.
    """
    response: object = get_response(url, bar=False if not (verbose) else True)
    if (headers): # Observing headers can offer user more info.
        print_headers(response.headers)
    print_robots(response.text)


def main(args: list=sys.argv) -> None:
    headers: bool = False
    verbose: bool = False
    args_checked: list = [] # List of arg names that are already checked.
    url_simple: str = ""
    url_formatted: str = ""

    for index, arg in enumerate(args):
        if (index == 0):
            continue
        if (arg == "-H") or (arg == "--include-headers"):
            headers = True
            args_checked.append(arg)
        elif (arg == "-v") or (arg == "--verbose"):
            verbose = True
            args_checked.append(arg)
        if not(arg.startswith("-")):
            url_simple = arg

    if (url_simple):
        if (url_simple == "youtube"):
            url_formatted = "https://www.youtube.com/robots.txt"
        elif (url_simple == "google"):
            url_formatted = "https://www.google.fi/robots.txt"
        else:
            sys.exit("{}: Info: '{}' not recognized ..".format(args[0], url_simple))

        print_all(
                url_formatted,
                verbose=False if not (verbose) else True,
                headers=False if not (headers) else True
                )


if (__name__ == "__main__"):
    main()
