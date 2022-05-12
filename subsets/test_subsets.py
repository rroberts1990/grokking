from subsets.subsets import Subsets
import pytest

@pytest.mark.parametrize('input, expected',
                         [([1, 3], [[], [1], [3], [1,3]]),
                          ([1, 5, 3], [[], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3]])])
def test_subsets(input, expected):
    solver = Subsets()
    actual = solver.subsets(input)
    assert actual == expected