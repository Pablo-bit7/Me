#!/usr/bin/env python3
"""
Tests for `shorten()`
"""
from twttr import shorten


def test_shorten():
    assert shorten("Twitter") == "Twttr"
    assert shorten("What's your name?") == "Wht's yr nm?"
    assert shorten("CS50") == "CS50"
    assert shorten("PYTHON") == "PYTHN"


if __name__ == "__main__":
    test_shorten()
