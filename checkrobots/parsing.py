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
        self.quiet: bool = False
        self.headers: bool = False
        self.url_simple: str = ""
        self.invalid_args: list = []

        # All the different kinds of invalid chars or
        # char sequences etc. that we don't want
        # to approve as prefixes.
        #
        # New chars can be added here, by making a own
        # own section for those chars (like there is the
        # section for "hyphens").
        self.invalid_prefixes: dict = {
                "hyphens": [
                    "-" * index for index, i in enumerate(range(25), 3)
                    ],
                }

    def __str__(self) -> str:
        return f"Short args: {self.opts_short}, long args: {self.opts_long}"

    def __repr__(self) -> str:
        return f"ParseArgs(args={self.args!r})"

    def sort_args_invalid(self, arg: str) -> None:
        for invalid_prefix in self.invalid_prefixes["hyphens"]:
            if (arg.startswith(invalid_prefix)):
                self.invalid_args.append(arg)

    def sort_args_valid(self, arg: str) -> None:
        if (arg.startswith("--")):
            self.opts_long.append(arg)
        elif (arg.startswith("-")):
            self.opts_short.append(arg)
        else:
            if not (self.url_simple):
                self.url_simple = arg

    def sort_args(self) -> None:
        for index, arg in enumerate(self.args):
            if (index == 0):
                continue
            self.sort_args_invalid(arg)
            self.sort_args_valid(arg)

    def parse_args_short(self) -> None:
        for arg in self.opts_short:
            for index, char in enumerate(arg):
                if (index == 0):
                    continue
                if (char == "q"):
                    self.quiet = True
                elif (char == "H"):
                    self.headers = True

    def parse_args_long(self) -> None:
        for arg in self.opts_long:
            if (arg == "--quiet"):
                self.quiet = True
            elif (arg == "--headers"):
                self.headers = True
            else:
                self.invalid_args.append(arg)

    def parse_args(self) -> None:
        self.sort_args()
        if (self.opts_short):
            self.parse_args_short()
        if (self.opts_long):
            self.parse_args_long()

    def is_quiet(self) -> bool:
        # Always override verbose/degub -flag(s) if quiet -flag is present.
        if (self.quiet):
            return True
        else:
            return False

    def is_headers(self) -> bool:
        return self.headers

    def get_invalid_args(self) -> list:
        return self.invalid_args

    def get_url_simple(self) -> str:
        return self.url_simple
