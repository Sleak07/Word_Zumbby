import pytest

from main import main


def test_add_positive_numbers():
    """test twopositive numbers"""
    assert main(2, 3) == 5


def test_add_negative_numbers():
    """test twopositive numbers"""
    assert main(-2, -3) == -5
