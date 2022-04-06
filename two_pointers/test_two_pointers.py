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