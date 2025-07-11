# Leetcode 945 - Minimum Increment to Make Array Unique

from typing import List

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        moves = 0
        
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                moves += (nums[i - 1] + 1 - nums[i])
                nums[i] = nums[i - 1] + 1
        
        return moves
