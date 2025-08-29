#!/usr/bin/env python3
"""
Outputs whether it's breakfast, lunch, or dinner time
"""

def main():
    while True:
        time = input("Wha time is it? ")
        print(convert(time))

def convert(time):
    hrs_min = time.strip().split(":")
    if hrs_min[0][0] == "0":
        hrs_min[0] = hrs_min[0][1]
    #if hrs_min[1][0] == "0":
    #    hrs_min[1] = hrs_min[1][1]

    if hrs_min[0] == "7" and int(hrs_min[1]) in range(60):
        return "breakfast time"
    elif hrs_min[0] == "8" and hrs_min[1] == "00":
        return "breakfast time"
    elif hrs_min[0] == "12" and int(hrs_min[1]) in range(60):
        return "lunch time"
    elif hrs_min[0] == "13" and hrs_min[1] == "00":
        return "lunch time"
    elif hrs_min[0] == "18" and int(hrs_min[1]) in range(60):
        return "dinner time"
    elif hrs_min[0] == "19" and hrs_min[1] == "00":
        return "dinner time"


if __name__ == "__main__":
    main()