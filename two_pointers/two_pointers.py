from collections import deque
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

    def triplets_with_smaller_sum(self, arr, target):
        arr.sort()
        count = 0
        for i in range(len(arr)-2):
            count += self.search_pair_smaller_sum(arr, target - arr[i], i)
        return count

    def search_pair_smaller_sum(self, arr, target_sum, first):
        count = 0
        left, right = first + 1, len(arr) - 1
        while left < right:
            if arr[left] + arr[right] < target_sum:
                count += right - left
                left += 1
            else:
                right -= 1
        return count

    def subarrays_with_product_less_than_tgt(self, arr, target):
        result = []
        product = 1
        left = 0
        for right in range(len(arr)):
            product *= arr[right]
            while (product >= target and left < len(arr)):
                product /= arr[left]
                left += 1
            temp_list = deque()
            for i in range(right, left-1, -1):
                temp_list.appendleft(arr[i])
                result.append(list(temp_list))
        return result


    def quad_sum_to_target(self, arr, target):
        arr.sort()
        result = []
        for i in range(len(arr) - 3):
            if i > 0 and arr[i] == arr[i-1]:
                continue
            for j in range(i + 1, len(arr) - 2):
                if j > i + 1 and arr[j] == arr[j - 1]:
                    continue
                self.search_triplet(arr,target, i, j, result)
        return result


    def search_triplet(self, arr, target_sum, first, second, quadruplets):
        left = second + 1
        right = len(arr) - 1
        while left < right:
            quad_sum = arr[first] + arr[second] + arr[left] + arr[right]
            if quad_sum == target_sum:
                quadruplets.append([arr[first], arr[second], arr[left], arr[right]])
                left += 1
                right -= 1
                while (left < right and arr[left] == arr[left-1]):
                    left += 1
                while (left < right and arr[right] == arr[right + 1]):
                    right -= 1
            elif quad_sum < target_sum:
                left += 1
            else:
                right -= 1

    def dutch_flag(self, arr):
        low = 0
        high = len(arr) - 1
        i = 0
        while i <= high:
            if arr[i] == 0:
                arr[i], arr[low] = arr[low], arr[i]
                i += 1
                low += 1
            elif arr[i] == 1:
                i += 1
            else:
                arr[i], arr[high] = arr[high], arr[i]
                high -= 1
        return arr

    def strings_with_backspaces(self, str1, str2):
        idx1 = len(str1) - 1
        idx2 = len(str2) - 1

        while idx1 >= 0 or idx2 >= 0:
            i1 = self.get_next_valid_char_index(str1, idx1)
            i2 = self.get_next_valid_char_index(str2, idx2)
            if i1 < 0 and i2 < 0:
                return True
            if i1 < 0 or i2 < 0:
                return False
            if str1[i1] != str2[i2]:
                return False

            idx1 = i1 - 1
            idx2 = i2 - 1
        return True


    def get_next_valid_char_index(self, str, index):
        backspace_count = 0
        while index >= 0:
            if str[index] == '#':
                backspace_count += 1
            elif backspace_count > 0:
                backspace_count -= 1
            else:
                break
            index -= 1
        return index

    def minimum_window_sort(self, arr):
        low, high = 0, len(arr) - 1
        while (low < len(arr) - 1 and arr[low] <= arr[low + 1]):
            low += 1
        if low == len(arr) - 1:
            return 0

        while (high > 0 and arr[high] >= arr[high - 1]):
            high -= 1

        subarray_max = -math.inf
        subarray_min = math.inf
        for k in range(low, high+1):
            subarray_max = max(subarray_max, arr[k])
            subarray_min = min(subarray_min, arr[k])

        while low > 0 and arr[low-1] > subarray_min:
            low -= 1
        while high > len(arr) - 1 and arr[high+1] < subarray_max:
            high += 1
        return high - low + 1