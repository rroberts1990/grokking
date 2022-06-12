from sorting.sorting import Sorting
import pytest


def test_merge_sort():
    input = [1, 4, 2, 6, 0, 3]
    sorter = Sorting(input)
    sorter.merge_sort()
    actual = sorter.A
    assert actual == [0, 1, 2, 3, 4, 6]


def build(arr):
    A = [x for x in arr]
    def build_subtree(A, i ,j):
        c = (i + j)//2



