#!/usr/bin/env python3
"""
Tests for the `jar.py` program
"""
import pytest
from jar import Jar


def test_init():
    """Test Jar initialization with default and custom capacity"""
    jar = Jar()
    assert jar.capacity == 12
    jar = Jar(10)
    assert jar.capacity == 10
    with pytest.raises(ValueError):
        Jar(0)
    with pytest.raises(ValueError):
        Jar(-1) 


def test_str():
    """Test string representation of the jar"""
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    """Test depositing cookies into the jar"""
    jar = Jar()
    jar.deposit(3)
    assert jar.size == 3
    jar.deposit(8)
    assert jar.size == 8
    with pytest.raises(ValueError):
        jar.deposit(10)


def test_withdraw():
    """Test withdrawing cookies from the jar"""
    jar = Jar()
    jar.deposit(10)
    jar.withdraw(3)
    assert jar.size == 7
    jar.withdraw(5)
    assert jar.size == 2
    with pytest.raises(ValueError):
        jar.withdraw(5)


if __name__ == "__main__":
    pytest.main([__file__])
