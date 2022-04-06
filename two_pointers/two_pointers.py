
import math
class TwoPointers:

    def pair_with_target_sum(self, array, target):
        left, right = 0, len(array) - 1
        while left < right:
            current = (array[left] + array[right])
            if current == target:
                return [left, right]
            elif current > target:
                right -= 1
            elif current < target:
                left += 1
        return [-1, -1]

    def pair_with_target_sum_hashtable(self, array, target):
        hash_map = {}
        for i in range(len(array)):
            complement = target - array[i]
            if complement in hash_map:
                return [hash_map[complement], i]
            hash_map[array[i]] = i
        return [-1, -1]

    def remove_duplicates(self, array):
        next_non_dupe = 1
        i = 0

        while i < len(array):
            print(f'i is {i}')
            print(f'next_non_dupe is {next_non_dupe}')
            if array[next_non_dupe - 1] != array[i]:
                array[next_non_dupe] = array[i]
                next_non_dupe += 1
            i += 1
        return next_non_dupe


    def square_sorted_array(self, array):
        n = len(array)
        squares = [0 for x in range(n)]
        largest_square_idx = n - 1
        left, right = 0, n - 1
        while left <= right:
            left_square = array[left] * array[left]
            right_square = array[right] * array[right]
            if left_square > right_square:
                squares[largest_square_idx] = left_square
                left += 1
            else:
                squares[largest_square_idx] = right_square
                right -= 1
            largest_square_idx -= 1
        return squares

    def triplet_sum_to_zero(self, array):
        triplets = []
        array.sort()

        for i in range(len(array)):
            if i > 0 and array[i] == array[i-1]:
                continue
            self.search_pair(array, -array[i], i+1, triplets)
        return triplets

    def search_pair(self, arr, target_sum, left, triplets):
        right = len(arr) - 1

        while left < right:
            current_sum = arr[left] + arr[right]
            if current_sum == target_sum:
                triplets.append([-target_sum, arr[left], arr[right]])
                left += 1
                right -= 1
                while left < right and arr[left] == arr[left-1]:
                    left += 1
                while left < right and arr[right] == arr[right+1]:
                    right -= 1
            elif target_sum > current_sum:
                left += 1
            else:
                right -= 1


    def triplet_sum_close_to_tgt(self, arr, target):
        arr.sort()
        smallest_diff = math.inf
        for i in range(len(arr)-2):
            left = i + 1
            right = len(arr) - 1
            while left < right:
                target_diff = target - arr[i] - arr[left] - arr[right]
                if target_diff == 0:
                    return target
                if abs(target_diff) < abs(smallest_diff) or (abs(target_diff) == abs(smallest_diff) and
                target_diff > smallest_diff):
                    smallest_diff = target_diff
                if target_diff > 0:
                    left += 1
                else:
                    right -= 1

        return target - smallest_diff
