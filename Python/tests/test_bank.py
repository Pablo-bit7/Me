#!/usr/bin/env python3
"""
Tests for the Seinfeld bank program
"""
from bank import value


def test_value():
    assert value("Hello") == "$0"
    assert value(" Hello ") == "$0"
    assert value("Hello, Newman") == "$0"
    assert value("How you doing?") == "$20"
    assert value("What's happening?") == "$100"
    assert value("What's up?") == "$100"


if __name__ == "__main__":
    test_value()
