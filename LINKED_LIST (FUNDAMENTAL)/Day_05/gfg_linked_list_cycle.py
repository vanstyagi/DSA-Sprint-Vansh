# This is the GFG platform question for just of practice purpose.

# Link : https://www.geeksforgeeks.org/problems/detect-loop-in-linked-list/1

class Solution:
    def detectLoop(self, head):
        # code here
        slow = head 
        fast = head 
        
        while fast is not None and fast.next is not None: 
            slow = slow.next
            fast = fast.next.next
            
            if fast == slow:
                return True
        return False