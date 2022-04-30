

class CyclicSort:

    def cyclic_sort(self, nums):
        i = 0

        while i < len(nums):
            print(i)
            print(nums)
            j = nums[i] - 1
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1

        return nums

    def find_missing_number(self, nums):
        i, n = 0, len(nums)
        while i < n:
            j = nums[i]
            if j < n and j != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1

        for i in range(n):
            if nums[i] != i:
                return i
        return n

    def find_all_missing_numbers(self, nums):
        i = 0
        missing_numbers = []
        while i < len(nums):
            j = nums[i] - 1
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1

        for i in range(len(nums)):
            if nums[i] != i + 1:
                missing_numbers.append(i + 1)

        return missing_numbers

    def find_duplicate_number(self, nums):
        i = 0

        while i < len(nums):
            if nums[i] != i + 1:
                j = nums[i] - 1
                if nums[i] != nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
                else:
                    return nums[i]
            else:
                i += 1

    def find_all_duplicate_numbers(self, nums):
        i = 0

        while i < len(nums):
            j = nums[i] - 1
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
        dupes = []
        for i in range(len(nums)):
            if nums[i] != i + 1:
                dupes.append(nums[i])
        return dupes

    def find_corrupt_pair(self, nums):
        i = 0
        while i < len(nums):
            j = nums[i] - 1
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return [nums[i], i + 1]

        return [-1, -1]

    def find_smallest_missing_positive(self, nums):
        i = 0

        while i < len(nums):
            j = nums[i] - 1
            if nums[i] > 0 and nums[i] <= len(nums) and nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1

    def find_first_k_missing(self, nums, k):
        i = 0
        missing = []
        n = len(nums)

        while i < n:
            j = nums[i] - 1
            if nums[i] > 0 and nums[i] <= n and nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1

        extra = set()
        for i in range(n):
            if len(missing) < k:
                if nums[i] != i + 1:
                    missing.append(i + 1)
                    extra.add(nums[i])
        i = 1
        while len(missing) < k:
            candidate = i + n
            if candidate not in extra:
                missing.append(candidate)
            i += 1
        return missing




