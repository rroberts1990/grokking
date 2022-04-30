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


@pytest.mark.parametrize('nums, expected',
                         [([4, 0, 3, 1], 2),
                          ([8, 3, 5, 2, 4, 6, 0, 1], 7)])
def test_find_missing_number(nums, expected):
    solver = CyclicSort()
    actual = solver.find_missing_number(nums)
    assert actual == expected


@pytest.mark.parametrize('nums, expected',
                         [([2, 3, 1, 8, 2, 3, 5, 1], [4, 6, 7]),
                          ([2, 4, 1, 2], [3]),
                          ([2, 3, 2, 1], [4])])
def test_find_all_missing_numbers(nums, expected):
    solver = CyclicSort()
    actual = solver.find_all_missing_numbers(nums)
    assert actual == expected


@pytest.mark.parametrize('nums, expected',
                         [([1, 4, 4, 3, 2], 4),
                          ([2, 1, 3, 3, 5, 4], 3),
                          ([2, 4, 1, 4, 4], 4)])
def test_find_duplicate_numbers(nums, expected):
    solver = CyclicSort()
    actual = solver.find_duplicate_number(nums)
    assert actual == expected


@pytest.mark.parametrize('nums, expected',
                         [([3, 4, 4, 5, 5], [5, 4]),
                          ([5, 4, 7, 2, 3, 5, 3], [3, 5])])
def test_find_all_duplicate_numbers(nums, expected):
    solver = CyclicSort()
    actual = solver.find_all_duplicate_numbers(nums)
    assert actual == expected

@pytest.mark.parametrize('nums, expected',
                         [([3, 1, 2, 5, 2], [2, 4]),
                          ([3, 1, 2, 3, 6, 4], [3, 5])])
def test_find_corrupt_pairs(nums, expected):
    solver = CyclicSort()
    actual = solver.find_corrupt_pair(nums)
    assert actual == expected


@pytest.mark.parametrize('nums, expected',
                         [([-3, 1, 5, 4, 2], 3),
                          ([3, -2, 0, 1, 2], 4),
                          ([3, 2, 5, 1], 4),
                          ([33, 37, 5], 1)])
def test_find_smalled_missing_positive(nums, expected):
    solver = CyclicSort()
    actual = solver.find_smallest_missing_positive(nums)
    assert actual == expected

@pytest.mark.parametrize('nums, k, expected',
                         [([3, -1, 4, 5, 5], 3, [1, 2, 6]),
                          ([2, 3, 4], 3, [1, 5, 6]),
                          ([-2, -3, 4], 2, [1, 2])])
def test_find_first_k_missing(nums, k, expected):
    solver = CyclicSort()
    actual = solver.find_first_k_missing(nums, k)
    assert actual == expected