class Solution(object):
    def moveZeroes(self, nums):
        n = len(nums)
        for i in range(n-1, -1, -1):  # Start from least significant digit
            if nums[i] < 9:
                nums[i] += 1
                return digits
            nums[i] = 0  # Carry over
        return [1] + nums
        