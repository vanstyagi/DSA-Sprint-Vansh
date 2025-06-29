# Leetcode 179 - Largest Number

from functools import cmp_to_key

class Solution(object):
    def largestNumber(self, nums):
        nums = list(map(str, nums))

        def compare(x, y):
            return -1 if x + y > y + x else 1

        nums.sort(key=cmp_to_key(compare))

        result = ''.join(nums)
        return '0' if result[0] == '0' else result
