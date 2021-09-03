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

# The name of this program. It is just
# the easiest to grab the name from the cmd
# line -args, which is always the first arg.
NAME: str = sys.argv[0]

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
    for index, pair in enumerate(sorted(headers.items()) if (sort) else headers.items()):
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
    if (scraping_not_suitable):
        print(dedent("""
        PLEASE NOTE: It seems that there were no 'allowed' 
        endpoint fields in the robots.txt that was fetched.
        This means, that you maybe shouldn't try to scrape
        the website (or, at least, if the tool you're using to
        scrape the website is going to be in public use and
        you don't have explicit permission from the website)."""))
    else:
        print("----- ROBOTS.TXT -----")
        endpoints: list = []
        for line in robots.split("\n"):
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
        allowed_endpoints: int = 0
        for line in response.text.split("\n"):
            if (line.startswith("Allow")):
                allowed_endpoints += 1
        if (verbose):
            print("[{}]: ".format(NAME), end="")
            print("{} allowed endpoints found ...".format(allowed_endpoints))
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
    response: object = get_response(url, verbose=False if not (verbose) else True)
    if (headers):
        headers_count: int = 1
        print_headers(response.headers)
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


def main(args: list=sys.argv) -> None:
    parsed: object = parsing.ParseArgs(args)
    parsed.parse_args()
    headers: bool = parsed.is_headers()
    verbose: bool = parsed.is_verbose()
    invalid_args: list = parsed.get_invalid_args()
    url_simple: str = parsed.get_url_simple()
    url_formatted: str = ""

    if (invalid_args):
        sys.exit(1)

    if (url_simple):
        url_formatted = gen_long_url(url_simple) 
        print_all(url_formatted, verbose=False if not (verbose) else True,
                  headers=False if not (headers) else True,)
    else:
        sys.exit(dedent("""
                {0} {1}, utility that can check websites robots.txt.
                Usage: {0} [options] <website_name>
                """.format(NAME, VERSION)).strip())


if (__name__ == "__main__"):
    main()
