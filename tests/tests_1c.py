"""
tests_1c.py

This module contains unit tests for the max_subarray_sum function defined in lab_1c.py.
"""

import pytest
from labs.lab_1.lab_1c import max_subarray_sum
def test():
    assert max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4]) == 6 ## test regular case
    assert max_subarray_sum([-2,-1,-3,-4,-1,-2,-1,-5,-4]) == -1 #test when all nums are negative
    assert max_subarray_sum([0, 0, 0, 0, 0, 0]) == 0 # test when all values are zero


if __name__ == "__main__":
    pytest.main()