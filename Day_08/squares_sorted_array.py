# LeetCode 977: Squares of a Sorted Array
# ✅ Two pointer from both ends, insert in reverse

class Solution(object):
    def sortedSquares(self, nums):
        res = [0] * len(nums)
        left, right = 0, len(nums) - 1
        pos = len(nums) - 1

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                res[pos] = nums[left] ** 2
                left += 1
            else:
                res[pos] = nums[right] ** 2
                right -= 1
            pos -= 1

        return res
