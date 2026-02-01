def isPalindrome(self, head):
        values = []
        current = head 
        while current:
            values.append(current.val)
            current = current.next

        left, right = 0, len(values) - 1
        while left < right:
            if values[left] != values[right]:
                return False
            left += 1
            right -= 1
        return True