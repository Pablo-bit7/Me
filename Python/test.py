#!/usr/bin/env python3

def print_numbers(n):
    if n == 0:
        return
    print(n)
    print_numbers(n-1)

if __name__ == '__main__':
    print_numbers(5)