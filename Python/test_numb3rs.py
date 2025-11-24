#!/usr/bin/env python3
"""
Tests for the `numb3rs` program
"""
import pytest
from numb3rs import validate


def test_valid_ip():
    """Test valid IP address"""
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True


def test_invalid_ip():
    """Test invalid IP address"""
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False
    assert validate("192.168.001.1") == False
    assert validate("cat") == False


if __name__ == "__main__":
    pytest.main([__file__])
