# This is the GFG question [ https://www.geeksforgeeks.org/problems/nth-node-from-end-of-linked-list/1 ]

class Solution:
    def getKthFromLast(self, head, k):
    
        fast = slow = head
        for _ in range(k):
            if not fast:
                return - 1
            fast = fast.next
            
        if not fast:
            return head.data
            
        while fast.next:
            slow = slow.next
            fast = fast.next
            
        return slow.next.data