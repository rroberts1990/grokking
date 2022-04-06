

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


# [2, 3, 3, 3, 6, 9, 9], 4