#!/usr/bin/env python3
"""
Program prompts user for a date (MM/DD/YYYY), and outputs it in YYYY-MM-DD format
"""


def main():
    months = {
        "January": "01",
        "February": "02",
        "March": "03",
        "April": "04",
        "May": "05",
        "June": "06",
        "July": "07",
        "August": "08",
        "September": "09",
        "October": "10",
        "November": "11",
        "December": "12"
    }

    while True:
        date = input("Date: ").strip()

        try:
            if "/" in date:
                parsed_date = date.split("/")

                if int(parsed_date[0]) in range(1, 13) and int(parsed_date[1]) in range(1, 32):
                    for i, char in enumerate(parsed_date):
                        if len(char) == 1:
                            parsed_date[i] = "0" + char
                else:
                    continue

            elif ", " in date:
                parsed_date = date.split(" ")

                if parsed_date[0].isdigit():
                    continue

                for i, char in enumerate(parsed_date):
                    parsed_date[i] = char.replace(",", "")
                    if parsed_date[i] in months:
                        parsed_date[i] = months[parsed_date[i]]
                
                if int(parsed_date[0]) in range(1, 13) and int(parsed_date[1]) in range(1, 32):
                    for i, char in enumerate(parsed_date):
                        if len(char) == 1:
                            parsed_date[i] = "0" + char
                else:
                    continue
            
            else:
                continue
    
        except ValueError:
            continue

        else:
            print(f"{parsed_date[2]}-{parsed_date[0]}-{parsed_date[1]}")
            break


if __name__ == "__main__":
    main()
