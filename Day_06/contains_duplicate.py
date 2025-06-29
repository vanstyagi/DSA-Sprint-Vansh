# Leetcode 217 - Contains Duplicate

class Solution(object):
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))
