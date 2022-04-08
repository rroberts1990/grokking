import pytest

from two_pointers.two_pointers import TwoPointers


@pytest.mark.parametrize('input, target, expected',
                         [([1, 2, 3, 4, 6], 6, [1, 3]),
                          ([2, 5, 9, 11], 11, [0, 2])])
def test_pair_with_target_sum(input, target, expected):
    solver = TwoPointers()
    actual = solver.pair_with_target_sum(input, target)
    assert actual == expected

@pytest.mark.parametrize('input, target, expected',
                         [([1, 2, 3, 4, 6], 6, [1, 3]),
                          ([2, 5, 9, 11], 11, [0, 2])])
def test_pair_with_target_sum_hashtable(input, target, expected):
    solver = TwoPointers()
    actual = solver.pair_with_target_sum_hashtable(input, target)
    assert actual == expected

@pytest.mark.parametrize('input, expected',
                         [([2, 3, 3, 3, 6, 9, 9], 4),
                          ([2, 2, 2, 11], 2)])
def test_remove_duplicates(input, expected):
    solver = TwoPointers()
    actual = solver.remove_duplicates(input)
    assert actual == expected

@pytest.mark.parametrize('input, expected',
                         [([-2, -1, 0, 2, 3], [0, 1, 4, 4, 9]),
                          ([-3, -1, 0, 1, 2], [0, 1, 1, 4, 9])])
def test_square_sorted_array(input, expected):
    solver = TwoPointers()
    actual = solver.square_sorted_array(input)
    assert actual == expected

@pytest.mark.parametrize('input, expected',
                         [([-3, 0, 1, 2, -1, 1, -2], [[-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]]),
                          ([-5, 2, -1, -2, 3], [[-5, 2, 3], [-2, -1, 3]])])
def test_triplet_sum_to_zero(input, expected):
    solver = TwoPointers()
    actual = solver.triplet_sum_to_zero(input)
    assert actual == expected

@pytest.mark.parametrize('input, target, expected',
                         [([-2, 0, 1, 2], 2, 1),
                          ([-3, -1, 1, 2], 1, 0),
                          ([1, 0, 1, 1], 100, 3)])
def test_triplet_sum_close_to_tgt(input, target, expected):
    solver = TwoPointers()
    actual = solver.triplet_sum_close_to_tgt(input, target)
    assert actual == expected

@pytest.mark.parametrize('input, target, expected',
                                  [([-1, 0, 2, 3], 3, 2),
                                   ([-1, 4, 2, 1, 3], 5, 4)])
def test_triplet_with_smaller_sum(input, target, expected):
    solver = TwoPointers()
    actual = solver.triplets_with_smaller_sum(input, target)
    assert actual == expected

@pytest.mark.parametrize('input, target, expected',
                         [([2, 5, 3, 10], 30, [[2], [5], [2, 5], [3], [5, 3], [10]]),
                          ([8, 2, 6, 5], 50, [[8], [2], [8, 2], [6], [2, 6], [5], [6, 5]])])
def test_subarrays_with_product_less_than_tgt(input, target, expected):
    solver = TwoPointers()
    actual = solver.subarrays_with_product_less_than_tgt(input, target)
    assert actual == expected


@pytest.mark.parametrize('input, target, expected',
                         [([4, 1, 2, -1, 1, -3], 1, [[-3, -1, 1, 4], [-3, 1, 1, 2]]),
                          ([2, 0, -1, 1, -2, 2], 2, [[-2, 0, 2, 2], [-1, 0, 1, 2]])])
def test_quad_sum_to_target(input, target, expected):
    solver = TwoPointers()
    actual = solver.quad_sum_to_target(input, target)
    assert actual == expected

@pytest.mark.parametrize('input, expected',
                         [([1, 0, 2, 1, 0], [0, 0, 1, 1, 2]),
                          ([2, 2, 0, 1, 2, 0], [0, 0, 1, 2, 2, 2])])
def test_dutch_flag(input, expected):
    solver = TwoPointers()
    actual = solver.dutch_flag(input)
    assert actual == expected

@pytest.mark.parametrize('str1, str2, expected',
                         [("xy#z", "xzz#", True),
                          ("xy#z", "xyz#", False),
                          ("xp#", "xyz##", True),
                          ("xywrrmp", "xywrrmu#p", True)])
def test_strings_with_backspaces(str1, str2, expected):
    solver = TwoPointers()
    actual = solver.strings_with_backspaces(str1, str2)
    assert actual == expected

@pytest.mark.parametrize('arr, expected',
                         [([1, 2, 5, 3, 7, 10, 9, 12], 5),
                          ([1, 3, 2, 0, -1, 7, 10], 5),
                          ([1, 2, 3], 0),
                          ([3, 2, 1], 3)])
def test_minimum_window_sort(arr, expected):
    solver = TwoPointers()
    actual = solver.minimum_window_sort(arr)
    assert actual == expected