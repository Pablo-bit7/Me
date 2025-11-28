#!/usr/bin/env python3
"""
Program expects an IPv4 string and returns `True` if it is a valid address,
and `False` otherwise
"""
import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if not re.search(r"^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$", ip):
        return False

    octet = ip.split(".")

    for num in octet:
        if len(num) > 1 and num.startswith("0"):
            return False

        value = int(num)

        if value < 0 or value > 255:
            return False

    return True


if __name__ == "__main__":
    main()
