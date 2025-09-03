import pytest

from para import add


def test_add_num():
    assert add(1, 2 == 3)


def test_add_strings():
    assert add("a", "b" == "ab")


# parametrize help to write same test for various conditions by changing only parameters
@pytest.mark.parametrize("a,b,c", [(1, 2, 3), ("a", "b", "ab")])
def test_add(a, b, c):
    assert a + b == c
