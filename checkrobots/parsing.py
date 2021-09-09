"""
parsing.py – Gather and parse command line arguments.
Author: Niklas Larsson
Date: September 2, 2021
"""


class ParseArgs:
    def __init__(self, args: list) -> None:
        self.args: list = args
        self.opts_short: list = []
        self.opts_long: list = []
        self.quiet: bool = False
        self.headers: bool = False
        self.sort: bool = False
        self.website: str = ""
        self.raw: bool = False
        self.invalid_args: list = []
        self.help_requested: bool = False
        self.version_requested: bool = False
        self.endpoints: dict = {
                "all": False,
                "disallowed": False,
                "allowed": True
                }

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
            if not (self.website):
                self.website = arg

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
                elif (char == "s"):
                    self.sort = True
                elif (char == "d"):
                    if not (self.endpoints["all"]):
                        self.endpoints["disallowed"] = True
                        self.endpoints["allowed"] = False
                elif (char == "a"):
                    self.endpoints["all"] = True
                    self.endpoints["allowed"] = False
                    self.endpoints["disallowed"] = False
                elif (char == "h"):
                    if (self.version_requested):
                        self.version_requested = False
                    self.help_requested = True
                elif (char == "V"):
                    if not (self.help_requested):
                        self.version_requested = True
                elif (char == "r"):
                    self.raw = True
                else:
                    self.invalid_args.append(char)

    def parse_args_long(self) -> None:
        for arg in self.opts_long:
            if (arg == "--quiet"):
                self.quiet = True
            elif (arg == "--headers"):
                self.headers = True
            elif (arg == "--sort"):
                self.sort = True
            elif (arg == "--disallowed"):
                if not (self.endpoints["all"]):
                    self.endpoints["disallowed"] = True
                    self.endpoints["allowed"] = False
            elif (arg == "--all"):
                self.endpoints["all"] = True
                self.endpoints["allowed"] = False
                self.endpoints["disallowed"] = False
            elif (arg == "--help"):
                if (self.version_requested):
                    self.version_requested = False
                self.help_requested = True
            elif (arg == "--version"):
                if not (self.help_requested):
                    self.version_requested = True
            elif (arg == "--raw"):
                self.raw = True
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

    def is_sort(self) -> bool:
        return self.sort

    def is_allowed(self) -> bool:
        return self.endpoints["allowed"]

    def is_disallowed(self) -> bool:
        return self.endpoints["disallowed"]

    def is_all(self) -> bool:
        return self.endpoints["all"]

    def is_help(self) -> bool:
        return self.help_requested

    def is_version(self) -> bool:
        return self.version_requested

    def is_raw(self) -> bool:
        return self.raw

    def get_invalid_args(self) -> list:
        return self.invalid_args

    def get_website_name(self) -> str:
        return self.website
