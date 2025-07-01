# LeetCode 680: Valid Palindrome II
# ✅ Two pointer with one skip allowed

class Solution(object):
    def validPalindrome(self, s):
        def is_valid_range(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return is_valid_range(left + 1, right) or is_valid_range(left, right - 1)
            left += 1
            right -= 1
        return True
