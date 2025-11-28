#!/usr/bin/env python3
"""
Program expects an HTML string, extracts any YouTube URL in any `iframe`
element therin, and returns its shorter, shareable equivalent.
"""
import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if re.search(r"<iframe(.)*><\/iframe>", s):

        url_pattern = re.search(r"(http)(s)?:\/\/(www\.)?youtube\.com\/embed\/([a-z_A-Z_0-9]+)", s)

        if url_pattern:
            url_parts = url_pattern.groups()
            return f"https://youtu.be/{url_parts[-1]}"
        else:
            return None

    else:
        return None


if __name__ == "__main__":
    main()
