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
            char_map[right_char] += 1
            while len(char_map) > k:
                left_char = string[window_start]
                char_map[left_char] -= 1
                if char_map[left_char] == 0:
                    del char_map[left_char]
                window_start += 1
            max_len = max(max_len, window_end - window_start + 1)
        return max_len



