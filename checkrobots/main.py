"""
main.py – Web 'spider' that checks sites, and if they allow webscraping.
Author: Niklas Larsson
Date: 29.8.2021
"""

import colourcodes
import parsing

import requests
import sys
import os
from textwrap import dedent


# This will be used to determine the language this
# program generally will output its information with.
LANG: str = os.getenv("LANG")

NAME: str = "checkrobots"
VERSION: str = "1.0"


def print_headers(headers: dict, sort: bool=True) -> None:
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
    if (sort):
        for index, pair in enumerate(sorted(headers.items())):
            print("{}: {}".format(pair[key], pair[value]))
    else:
        for index, pair in enumerate(headers.items()):
            print("{}: {}".format(pair[key], pair[value]))


def print_robots(robots_txt: str, sort: bool=True) -> None:
    """
    Print request's robots.txt's contents.

    Parameters
    ----------
    robots_txt....... The actual robots.txt content in plain/text.
    sort......... Alphabetically sort the 'rool' fields.
    """
    scraping_suitable: bool = "Allow" in robots_txt
    if (scraping_suitable):
        print("----- ROBOTS.TXT -----")
        endpoints: list = []
        for line in robots_txt.split("\n"):
            if (line.startswith("Allow")):
                endpoints.append(line.replace("Allow: ", ""))
        for index, line in enumerate(endpoints):
            print("Endpoint [{}] --> {}".format(index, line.strip()))


def get_response(url: str, verbose: bool) -> object:
    """
    Fetch the response object, A.K.A the robots.txt.

    Parameters
    ----------
    url........ Get the robots.txt of this url.
    verbose.... Print an indicator of sorts to indicate something's happening.
    """
    try:
        if (verbose):
            print("[{}]: Trying to fetch robots.txt ...".format(NAME))
            print("[Address]: {}".format(url))
        response: object = requests.get(url)
        if (verbose):
            print("[{}]: Fetched robots.txt successfully ...".format(NAME))
    except requests.ConnectionError as exception:
        sys.exit("{}: Error: Couldn't connect to {} ...".format(sys.argv[0], url))
    
    return response


def get_allowed_endpoints(response: object) -> int:
    """
    Check how many 'allowed' endpoints were found.

    Parameters
    ----------
    response....... The fetched response object.
    """
    allowed_endpoints: int = 0
    for line in response.text.split("\n"):
        if (line.startswith("Allow")):
            allowed_endpoints += 1

    return allowed_endpoints


def print_all(url: str, verbose: bool, headers: bool) -> None:
    """
    Print out all: the actual robots.txt, and additionally headers.
    
    Parameters
    ----------
    url.......... Use this url to fetch the robots.txt.
    verbose...... Let the output be a little more verbose.
    headers...... Also print the headers in addition to the robots.txt.
    """
    response: object = get_response(url, verbose=verbose)
    allowed_endpoints: int = get_allowed_endpoints(response)
    if (verbose):
        print("[{}]: ".format(NAME), end="")
        print("{} 'allowed' endpoints found ...".format(allowed_endpoints))
        if (headers):
            print()
            print_headers(response.headers)
        if (allowed_endpoints):
            print()
            print_robots(response.text)
    else:
        if (headers):
            print_headers(response.headers)
        if (allowed_endpoints):
            print()
            print_robots(response.text)


def gen_long_url(short_url: str) -> str:
    """
    Generate a valid, 'long' url from a 'shorter' url.

    Parameters
    ----------
    short_url...... 'Short' url, for example "google".
    """
    if (short_url == "youtube"):
        long_url = "https://www.youtube.com/robots.txt"
    elif (short_url == "google"):
        long_url = "https://www.google.fi/robots.txt"
    else:
        sys.exit("{}: Error: '{}' is not recognized ...".format(NAME, short_url))

    return long_url


def print_invalid_args(invalid_args: list) -> None:
    """
    Print arguments that were invalid.

    Parameters
    ----------
    invalid_args....... List of invalid args.
    """
    print("{}: Error: Invalid arguments provided: ".format(NAME), end="")
    args: str = " ".join(
            "\"{}\"".format(invalid_arg) for invalid_arg in invalid_args
            )
    print("{}.".format(args))


def main(args: list=sys.argv) -> None:
    parsed: object = parsing.ParseArgs(args)
    parsed.parse_args()
    headers: bool = parsed.is_headers()
    quiet: bool = parsed.is_quiet()
    verbose: bool = False if (quiet) else True
    invalid_args: list = parsed.get_invalid_args()
    url_simple: str = parsed.get_url_simple()
    url_formatted: str = ""

    if (invalid_args):
        print_invalid_args(invalid_args)
        sys.exit(1)

    if (url_simple):
        url_formatted = gen_long_url(url_simple) 
        print_all(url_formatted, verbose, headers)
    else:
        sys.exit(dedent("""
                {0} {1}, utility that can check websites robots.txt.
                Usage: {0} [options] <website_name>
                """.format(NAME, VERSION)).strip())


if (__name__ == "__main__"):
    main()
