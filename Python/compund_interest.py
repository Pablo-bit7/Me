#!/usr/bin/env python3
"""
Function calculates compund interest
"""

def compound_interest(starting_balance, interest_rate, contribution, months):
    final_balance = starting_balance * (interest_rate) + contribution

    for i in range(1, months):
        print(final_balance)
        final_balance = final_balance * (interest_rate) + contribution
    
    return final_balance

if __name__ == '__main__':
    starting_balance = float(input("Starting balance?: "))
    interest_rate = float(input("Interest rate (decimal fraction)?: "))
    contribution = float(input("Your monthly deposit?: "))
    months = int(input("Number of months?: "))

    print(compound_interest(starting_balance, interest_rate, contribution, months))
