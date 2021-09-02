"""
parsing.py – Gather and parse command line arguments.
Author: Niklas Larsson
Date: 2.9.2021
"""

class ParseArgs:
    def __init__(self, args: list) -> None:
        self.args: list = args
        self.opts_short: list = []
        self.opts_long: list = []
        self.verbose: bool = False
        self.headers: bool = False
        self.url_simple: str = ""
        self.invalid_args: list = []
        self.invalid_prefixes: list = [
                "-" * index for index, i in enumerate(range(25), 3)
                ]

    def __str__(self) -> str:
        return f"Short args: {self.opts_short}, long args: {self.opts_long}"

    def __repr__(self) -> str:
        return f"ParseArgs(args={self.args!r})"

    def sort_args(self) -> None:
        for index, arg in enumerate(self.args):
            if (index == 0):
                continue
            for invalid_prefix in self.invalid_prefixes:
                if (arg.startswith(invalid_prefix)):
                    self.invalid_args.append(arg)
                elif (arg.startswith("--")):
                    self.opts_long.append(arg)
                elif (arg.startswith("-")):
                    self.opts_short.append(arg)
                else:
                    if not (self.url_simple):
                        self.url_simple = arg

    def parse_args_short(self) -> None:
        for arg in self.opts_short:
            for index, char in enumerate(arg):
                if (index == 0):
                    continue
                self.verbose = char == "v"
                self.headers = char == "H"

    def parse_args_long(self) -> None:
        for arg in self.opts_long:
            self.verbose = arg == "--verbose"
            self.headers = arg == "--headers"

    def parse_args(self) -> None:
        self.sort_args()
        self.parse_args_short()
        self.parse_args_long()

    def is_verbose(self) -> bool:
        return self.verbose

    def is_headers(self) -> bool:
        return self.headers

    def get_invalid_args(self) -> list:
        return self.invalid_args

    def get_url_simple(self) -> str:
        return self.url_simple
