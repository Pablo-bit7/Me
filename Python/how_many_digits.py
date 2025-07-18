#!/usr/bin/env python3
"""
Function takes an int and returns how many digits it has
"""

def how_many_digits(number):
    return len(str(abs(number)))

    count = 0
    number = abs(number)

    if number == 0:
        return 1
    
    while number > 0:
        number //= 10
        count += 1
    
    return count

if __name__ == '__main__':
    print(how_many_digits(100))
