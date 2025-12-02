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

        if pattern_match:
            group = pattern_match.groups()
            cleaned_group = [item.replace(":", "") for item in group if item != None]

            am_pm_positions = [i for i, item in enumerate(cleaned_group) if item in ['AM', 'PM']]

            for i, char in enumerate(cleaned_group):
                if char == "PM":
                    if len(cleaned_group) == 4: # ['9', 'AM', '5', 'PM']
                        if cleaned_group[i - 1] != "12":
                            cleaned_group[i - 1] = int(cleaned_group[i - 1]) + 12

                    elif len(cleaned_group) == 5: # ['9', '00', 'AM', '5', 'PM']
                        if am_pm_positions == [2, 4]:
                            if cleaned_group[i - 2] != "12":
                                cleaned_group[i - 2] = int(cleaned_group[i - 2]) + 12
                        else:
                            if cleaned_group[i - 2] != "12":
                                cleaned_group[i - 2] = int(cleaned_group[i - 2]) + 12

                    elif len(cleaned_group) == 6: # ['9', '00', 'AM', '5', '00', 'PM']
                        if cleaned_group[i - 2] != "12":
                            cleaned_group[i - 2] = int(cleaned_group[i - 2]) + 12

            if len(cleaned_group) == 4:
                return f"{cleaned_group[0]}:00 to {cleaned_group[2]}:00"
            elif len(cleaned_group) == 5:
                if am_pm_positions == [2, 4]:
                    return f"{cleaned_group[0]}:{cleaned_group[1]} to {cleaned_group[3]}:00"
                else:
                    return f"{cleaned_group[0]}:00 to {cleaned_group[2]}:{cleaned_group[3]}"
            else:
                return f"{cleaned_group[0]}:{cleaned_group[1]} to {cleaned_group[3]}:{cleaned_group[4]}"

        else:
            raise ValueError

    except ValueError:
        sys.exit("Invalid input")


if __name__ == "__main__":
    main()
