

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