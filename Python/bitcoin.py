#!/usr/bin/env python3
"""
Program takes 1 command-line argument, the number of Bitcoin that they would
like to buy, then queries the CoinCap API Price Index
"""
import os
import sys
import requests


def main():
    try:
        if len(sys.argv) != 2:
            sys.exit("Missing command-line argument")

        else:
            api_key = os.getenv("COINCAP_API_KEY")
            r = requests.get(f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={api_key}")
            amount = float(r.json()["data"]["priceUsd"]) * float(sys.argv[1])
            
            print(f"${amount:,.4f}")

    except ValueError:
        sys.exit("Command-line argument is not a number")
    except requests.RequestException:
        print("An error occured")


if __name__ == "__main__":
    main()
