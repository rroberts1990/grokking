import pytest

from sliding_window.sliding_window import SlidingWindow

@pytest.mark.parametrize(
    'arr, k, expected',
    [([2, 1, 5, 1, 3, 2], 3, 9),
     ([2, 3, 4, 1, 5], 2, 7)]
)
def test_max_sum_subarray(arr, k, expected):
    solver = SlidingWindow()
    actual = solver.max_sum_subarray(arr, k)
    assert actual == expected

@pytest.mark.parametrize(
    'arr, s, expected',
    [([2, 1, 5, 2, 3, 2], 7, 2),
     ([2, 1, 5, 2, 8], 7, 1),
     ([3, 4, 1, 1, 6], 8, 3)]
)
def test_smallest_subarray(arr, s, expected):
    solver = SlidingWindow()
    actual = solver.smallest_subarray(arr, s)
    assert actual == expected

@pytest.mark.parametrize(
    'string, k, expected',
    [('araaci', 2, 4),
     ('araaci', 1, 2),
     ('cbbebi', 3, 5)]
)
def test_longest_substring_with_k_distinct_chars(string, k, expected):
    solver = SlidingWindow()
    actual = solver.longest_substring_with_k_distinct_chars(string, k)
    assert actual == expected


@pytest.mark.parametrize(
    'fruits, expected',
    [(['A', 'B', 'C', 'A', 'C'], 3),
    (['A', 'B', 'C', 'B', 'B', 'C'], 5)]
)
def test_fruits_into_baskets(fruits, expected):
    solver = SlidingWindow()
    actual = solver.fruits_into_baskets(fruits)
    assert actual == expected

@pytest.mark.parametrize(
    'string, expected',
    [('aabccbb', 3),
     ('abbbb', 2),
     ('abccde', 3)]
)
def test_longest_distinct_substring(string, expected):
    solver = SlidingWindow()
    actual = solver.longest_distinct_substring(string)
    assert actual == expected


@pytest.mark.parametrize(
    'string, k, expected',
    [('aabccbb', 2, 5),
     ('abbcb', 1, 4),
     ('abccde', 1, 3)]
)
def test_longest_substring_with_replacement(string, k, expected):
    solver = SlidingWindow()
    actual = solver.longest_substring_with_replacement(string, k)
    assert actual == expected


@pytest.mark.parametrize(
    'array, k, expected',
    [([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2, 6),
     ([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3, 9)]
)
def test_longest_substring_ones_with_replacement(array, k, expected):
    solver = SlidingWindow()
    actual = solver.longest_substring_ones_with_replacement(array, k)
    assert actual == expected

@pytest.mark.parametrize(
    'string, pattern, expected',
    [('oidbcaf', 'abc', True),
     ('odicf', 'dc', False),
     ('bcdxabcdy', 'bcdyabcdx', True),
     ('aaacb', 'abc', True)]
)
def test_permutations(string, pattern, expected):
    solver = SlidingWindow()
    actual = solver.permutations(string, pattern)
    assert actual == expected

@pytest.mark.parametrize(
    'string, pattern, expected',
    [('ppqp', 'pq', [1, 2]),
     ('abbcabc', 'abc', [2, 3, 4])]
)
def test_string_anagrams(string, pattern, expected):
    solver = SlidingWindow()
    actual = solver.string_anagrams(string, pattern)
    assert actual == expected


@pytest.mark.parametrize(
    'string, pattern, expected',
    [('aabdec', 'abc', 'abdec'),
     ('aabdec', 'abac', 'aabdec'),
     ('abdbca', 'abc', 'bca'),
     ('adcad', 'abc', '')]
)
def test_smallest_substring_containing_pattern(string, pattern, expected):
    solver = SlidingWindow()
    actual = solver.smallest_window_containing_pattern(string, pattern)
    assert actual == expected


@pytest.mark.parametrize(
    'string, words, expected',
    [('catfoxcat', ['cat', 'fox'], [0, 3]),
     ('catcatfoxfox', ['cat', 'fox'], [3])]
)
def test_words_concatenation(string, words, expected):
    solver = SlidingWindow()
    actual = solver.words_concatenation(string, words)
    assert actual == expected
