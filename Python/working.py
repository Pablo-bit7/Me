#!/usr/bin/env python3
"""
Program expects a `str` representing time in 12-hour format, and then
converts and returns the corresponding `str` in 24-hour format
"""
import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(time_12hr):
    try:
        pattern_match = re.search(r"^(1[0-2]|[1-9])(:[0-5][0-9])? (AM|PM) to (1[0-2]|[1-9])(:[0-5][0-9])? (AM|PM)$", time_12hr)

        if not pattern_match:
            raise ValueError
        
        groups = pattern_match.groups()

        hour_1 = int(groups[0])
        minutes_1 = groups[1][1:] if groups[1] else "00"
        period_1 = groups[2]

        hour_2 = int(groups[3])
        minutes_2 = groups[4][1:] if groups[4] else "00"
        period_2 = groups[5]

        if period_1 == "AM":
            if hour_1 == 12:
                hour_1 = 0
        else:
            if hour_1 != 12:
                hour_1 += 12

        if period_2 == "AM":
            if hour_2 == 12:
                hour_2 = 0
        else:
            if hour_2 != 12:
                hour_2 += 12

        return f"{hour_1:02d}:{minutes_1} to {hour_2:02d}:{minutes_2}"

    except ValueError:
        sys.exit("Invalid input")


if __name__ == "__main__":
    main()
