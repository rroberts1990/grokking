import pytest
from cyclic_sort.cyclic_sort import CyclicSort

@pytest.mark.parametrize('nums, expected',
                         [([3, 1, 5, 4, 2], [1, 2, 3, 4, 5]),
                          ([2, 6, 4, 3, 1, 5], [1, 2, 3, 4, 5, 6]),
                          ([1, 5, 6, 4, 3, 2], [1, 2, 3, 4, 5, 6])])
def test_cyclic_sort(nums, expected):
    solver = CyclicSort()
    actual = solver.cyclic_sort(nums)
    assert actual == expected

