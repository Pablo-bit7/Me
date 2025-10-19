#!/usr/bin/env python3
"""
Tests for the `fuel_1` program
"""
from fuel_1 import convert, gauge
import pytest


def test_convert_valid_fractions():
    """Test convert function with valid fractions"""
    assert convert("3/4") == 75
    assert convert("1/3") == 33
    assert convert("2/3") == 67
    assert convert("0/100") == 0
    assert convert("1/100") == 1
    assert convert("100/100") == 100
    assert convert("99/100") == 99


def test_convert_value_errors():
    """Test convert function raises ValueError for invalid inputs"""
    # X greater than Y
    with pytest.raises(ValueError):
        convert("10/3")
    
    # Non-integer inputs
    with pytest.raises(ValueError):
        convert("three/four")
    
    with pytest.raises(ValueError):
        convert("1.5/4")
    
    with pytest.raises(ValueError):
        convert("3/5.5")
    
    # Invalid format
    with pytest.raises(ValueError):
        convert("5-10")
    
    # Negative numbers
    with pytest.raises(ValueError):
        convert("-1/4")


def test_convert_zero_divisions():
    """Test convert function raises ZeroDivisionError"""
    with pytest.raises(ZeroDivisionError):
        convert("100/0")


def test_gauge_empty():
    """Test gauge function returns 'E' for low percentages"""
    assert gauge(0) == "E"
    assert gauge(1) == "E"


def test_gauge_full():
    """Test gauge function returns 'F' for high percentages"""
    assert gauge(99) == "F"
    assert gauge(100) == "F"


def test_gauge_percentage():
    """Test gauge function returns percentage for middle values"""
    assert gauge(75) == "75%"
    assert gauge(33) == "33%"
    assert gauge(67) == "67%"


if __name__ == "__main__":
    pytest.main([__file__])
