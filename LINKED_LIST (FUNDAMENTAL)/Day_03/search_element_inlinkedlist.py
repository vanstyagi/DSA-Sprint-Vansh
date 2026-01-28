# This is a GFG question  [ https://www.geeksforgeeks.org/problems/search-in-linked-list-1664434326/1 ]

class Solution:
    def searchKey(self, head, key):
        #Code here
        current = head
        
        while current:
            if current.data == key:
                return True
                
            current = current.next
        return False