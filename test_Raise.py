import pytest

from Raise import validate_age


def test_validate_age_valid_age():
    validate_age(20)


def test_validate_age_invalid_age():
    """
   This method tells pytest implicitly it's a known error
   and should not fail the test
    """
    with pytest.raises(ValueError,match="Age cannot be less than zero"):
        validate_age(-6)
