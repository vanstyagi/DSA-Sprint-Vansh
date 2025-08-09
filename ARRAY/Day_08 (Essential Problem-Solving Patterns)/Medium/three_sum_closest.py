# LeetCode 16: 3Sum Closest
# ✅ Similar to 3Sum with closest distance tracking

class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        closest = float('inf')

        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if abs(target - total) < abs(target - closest):
                    closest = total
                if total < target:
                    left += 1
                else:
                    right -= 1

        return closest
