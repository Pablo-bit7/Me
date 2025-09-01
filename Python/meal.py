#!/usr/bin/env python3
"""
Outputs whether it's breakfast, lunch, or dinner time
"""

def main():
    while True:
        time = input("Wha time is it? ")
        
        hrs_min = time.strip().split(":")
        if hrs_min[0][0] == "0":
            hrs_min[0] = hrs_min[0][1]

        if hrs_min[0] == "7" and int(hrs_min[1]) in range(60):
            print("breakfast time")
        elif hrs_min[0] == "8" and hrs_min[1] == "00":
            print("breakfast time")
        elif hrs_min[0] == "12" and int(hrs_min[1]) in range(60):
            print("lunch time")
        elif hrs_min[0] == "13" and hrs_min[1] == "00":
            print("lunch time")
        elif hrs_min[0] == "18" and int(hrs_min[1]) in range(60):
            print("dinner time")
        elif hrs_min[0] == "19" and hrs_min[1] == "00":
            print("dinner time")

def convert(time):
    hrs_min = time.strip().split(":")

    if hrs_min[0][0] == "0":
        hrs_min[0] = hrs_min[0][1]
    if hrs_min[1][0] == "0":
        hrs_min[1] = hrs_min[1][1]

    answer = int(hrs_min[0]) + int(hrs_min[1]) / 60
    return f"{answer} hours"


if __name__ == "__main__":
    main()