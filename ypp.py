#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
YAML PreProcesser
just simply replace `#!inc <filename> args...`
"""
import sys
import re

RE_INC = re.compile(r"^(\s*)#!inc\s+(.+)$")
RE_SPC = re.compile(r"\s+")
RE_VAR = re.compile(r"\$(\d+)")


def main(cmdline, indent=""):
    args = RE_SPC.split(cmdline)
    with open(args[0], "r", encoding="utf_8") as f:
        for row in f:
            m = RE_INC.match(row)
            if m:
                main(m.group(2), indent + m.group(1))
            else:
                print(indent + RE_VAR.sub(lambda m: args[int(m.group(1))], row), end="")


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        main(" ".join(sys.argv[1:]))
    else:
        main("template.yml")  # TODO: add some args
