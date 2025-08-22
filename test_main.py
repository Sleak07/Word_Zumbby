import pytest

from main import main

def test_addition_of_two_numbers():
    """Test addition of two numbers"""
    assert main(1, 2) == 3

def test_addition_of_two_negative_numbers():
    """Test addition of two negative numbers"""
    assert main(-1, -2) == -3

@pytest.mark.xfail(reason="Expected failure")
def test_addition_of_two_different_numbers():
    """Test addition of two negative numbers"""
    assert main(-1, -2) == 3
