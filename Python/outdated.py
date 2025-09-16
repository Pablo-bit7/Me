#!/usr/bin/env python3
"""
Program prompts user for a date (MM/DD/YYYY), and outputs it in YYYY-MM-DD format
"""


def main():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    while True:
        date = input("Date: ").strip()

        try:
            if "/" in date:
                parsed_date = date.split("/")
                
                for char in parsed_date:
                    if len(char) == 1:
                        char = "0" + char
            else:
                parsed_date = date.split(" ")
    
        except ValueError:
            continue


if __name__ == "__main__":
    main()
