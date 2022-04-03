from math import inf
from collections import defaultdict


class SlidingWindow:
    def max_sum_subarray(self, arr, k):
        window_start = 0
        max_sum = 0
        window_sum = 0

        for window_end in range(len(arr)):
            window_sum += arr[window_end]
            if window_end >= k - 1:
                max_sum = max(max_sum, window_sum)
                window_sum -= arr[window_start]
                window_start += 1
        return max_sum

    def smallest_subarray(self, arr, s):
        window_start = 0
        min_length = inf
        window_sum = 0

        for window_end in range(len(arr)):
            window_sum += arr[window_end]
            while window_sum >= s:
                min_length = min(min_length, window_end - window_start + 1)
                window_sum -= arr[window_start]
                window_start += 1
        return min_length

    def longest_substring_with_k_distinct_chars(self, string, k):
        window_start = 0
        max_len = 0
        char_map = defaultdict(int)

        for window_end in range(len(string)):
            right_char = string[window_end]
            char_map[right_char] += 1
            while len(char_map) > k:
                left_char = string[window_start]
                char_map[left_char] -= 1
                if char_map[left_char] == 0:
                    del char_map[left_char]
                window_start += 1
            max_len = max(max_len, window_end - window_start + 1)
        return max_len

    def fruits_into_baskets(self, fruits):
        window_start = 0
        most_fruits = 0
        fruit_map = defaultdict(int)

        for window_end in range(len(fruits)):
            right_fruit = fruits[window_end]
            fruit_map[right_fruit] += 1
            while len(fruit_map) > 2:
                left_fruit = fruits[window_start]
                fruit_map[left_fruit] -= 1
                if fruit_map[left_fruit] == 0:
                    del fruit_map[left_fruit]
                window_start += 1
            most_fruits = max(most_fruits, window_end - window_start + 1)
        return most_fruits

    def longest_distinct_substring(self, string):
        window_start = 0
        max_len = 0
        char_map = defaultdict(int)

        for window_end in range(len(string)):
            right_char = string[window_end]
            if right_char in char_map:
                window_start = max(window_start, char_map[right_char] + 1)
            char_map[right_char] = window_end
            max_len = max(max_len, window_end - window_start + 1)
        return max_len

    def longest_substring_with_replacement(self, string, k):
        window_start, max_repeat_letter_count, max_len = 0, 0, 0
        char_map = defaultdict(int)

        for window_end in range(len(string)):
            right_char = string[window_end]
            char_map[right_char] += 1
            max_repeat_letter_count = max(max_repeat_letter_count, char_map[right_char])
            if (window_end - window_start + 1 - max_repeat_letter_count) > k:
                left_char = char_map[window_start]
                char_map[left_char] -= 1
                window_start += 1
            max_len = max(max_len, window_end - window_start + 1)
        return max_len

    def longest_substring_ones_with_replacement(self, array, k):
        window_start, max_ones, max_len = 0, 0, 0

        for window_end in range(len(array)):
            right_val = array[window_end]
            if right_val == 1:
                max_ones += 1
            if (window_end - window_start + 1 - max_ones) > k:
                left_val = array[window_start]
                if left_val == 1:
                    max_ones -= 1
                window_start += 1
            max_len = max(max_len, window_end - window_start + 1)
        return max_len

    def permutations(self, string, pattern):
        window_start, matched = 0, 0
        char_map = defaultdict(int)

        for char in pattern:
            char_map[char] += 1

        for window_end in range(len(string)):
            right_char = string[window_end]
            if right_char in char_map:
                char_map[right_char] -= 1
                if char_map[right_char] == 0:
                    matched += 1
            if len(char_map) == matched:
                return True

            if window_end >= len(pattern) - 1:
                left_char = string[window_start]
                window_start += 1
                if left_char in char_map:
                    if char_map[left_char] == 0:
                        matched -= 1
                    char_map[left_char] += 1
        return False
