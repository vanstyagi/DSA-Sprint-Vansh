# LeetCode 344: Reverse String
# ✅ In-place two pointer swap

class Solution(object):
    def reverseString(self, s):
        left, right = 0, len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
