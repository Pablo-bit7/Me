#!/usr/bin/env python3
"""
Jar class - a simple container with a maximum capacity.
Supports depositing and withdrawing items and exposes `capacity` and `size`
properties
"""


class Jar:
    """A cookie jar with a fixed capacity."""

    def __init__(self, capacity=12):
        """Initialize jar with given capacity (default 12)"""
        if capacity <= 0:
            raise ValueError("Invalid capacity")

        self._capacity = capacity
        self._size = 0
        

    def __str__(self):
        """
        Return string representation of number of cookies in the jar with
        cookie emojis
        """
        return self.size * "🍪"


    def deposit(self, n):
        """Return string representation of jar with cookie emojis"""
        if n > self.capacity - self.size:
            raise ValueError("Cookie jar capacity exceeded")

        self._size += n


    def withdraw(self, n):
        """Remove n cookies from the jar"""
        if n > self.size:
            raise ValueError(f"There are only {self.size} cookies left in the jar")

        self._size -= n


    @property
    def capacity(self):
        """Maximum number of cookies the jar can hold"""
        return self._capacity


    @property
    def size(self):
        """Current number of cookies in the jar"""
        return self._size


if __name__ == "__main__":
    jar = Jar()
    print(f"Created jar with capacity {jar.capacity}")
    print(f"Current jar: {jar}")
    
    jar.deposit(5)
    print(f"After depositing 5 cookies: {jar}")
    print(f"Jar size: {jar.size}")
    
    jar.deposit(4)
    print(f"After depositing 4 more cookies: {jar}")
    print(f"Jar size: {jar.size}")
    
    jar.withdraw(3)
    print(f"After withdrawing 3 cookies: {jar}")
    print(f"Jar size: {jar.size}")
    
    try:
        jar.deposit(10)
    except ValueError as e:
        print(f"Error: {e}")

    try:
        jar.withdraw(20)
    except ValueError as e:
        print(f"Error: {e}")
