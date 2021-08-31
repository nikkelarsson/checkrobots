"""
main.py – Web 'spider' that checks sites, and if they allow webscraping.
Author: Niklas Larsson
Date: 29.8.2021
"""

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
        print("PLEASE NOTE, THAT WE DON'T ALLOW SCRAPING THIS SITE.")
    else:
        print("----- ROBOTS.TXT -----")
        endpoints: list = []
        for line in robots.split("\n"):
            if (line.startswith("Allow")):
                endpoints.append(line.replace("Allow: ", ""))
        for index, line in enumerate(endpoints):
            print("Endpoint [{}] --> {}".format(index, line.strip()))


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
        print("Fetched robots.txt ...") if (bar) else print(end="")
        allowed: int = 0
        for line in response.text.split("\n"):
            allowed += 1 if (line.startswith("Allow")) else 0
        print() if (bar) else print(end="")
        print("Found {} allowed endpoints ...".format(allowed))
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
        sys.exit("{}: Info: '{}' not recognized ..".format(NAME, short_url))

    return long_url


def main(args: list=sys.argv) -> None:
    headers: bool = False
    header_limit: bool = False
    header_limit_count: int
    verbose: bool = False
    args_checked: list = [] # List of arg names that are already checked.
    url_simple: str = ""
    url_formatted: str = ""

    # Go through the cmd line -args.
    for index, arg in enumerate(args):
        if (index == 0):
            continue

        # Check long flags (needs to be checked before short ones!).
        if (arg.startswith("--")):
            if (arg == "--verbose"):
                verbose = True
            elif (arg == "--headers"):
                headers = True

        # Check short flags.
        elif (arg.startswith("-")):
            for index, char in enumerate(arg):
                if (index == 0):
                    continue
                if (char == "H"):
                    headers = True
                elif (char == "v"):
                    verbose = True

        # Assume the arg is NOT a flag, when it
        # is not prefixed with hyphen(s) ('-').
        else:
            url_simple = arg

    # Fetch data and present it only if
    # a abbreviated url was present.
    # Program usage -message could be printed
    # otherwise, to show the user how to use the program.
    if (url_simple):
        url_formatted = gen_long_url(url_simple) 
        print_all(
                url_formatted,
                verbose=False if not (verbose) else True,
                headers=False if not (headers) else True,
                )
    else:
        sys.exit(dedent("""
                {0} {1}, utility that can check websites robots.txt.
                Usage: {0} [options] <short_url>
                """.format(NAME, VERSION)).strip())


if (__name__ == "__main__"):
    main()
