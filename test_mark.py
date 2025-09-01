import sys

import pytest

from mark import add


# skips the test if it marked using mark.skip unconditionally
@pytest.mark.skip(reason="Just testing to see if it skips")
def test_add_num():
    assert add(1, 2) == 3


# skipping the test on condition
@pytest.mark.skipif(sys.version_info > (3, 8), reason="Just skip it")
def test_add_num1():
    assert add(2, 3) == 5
