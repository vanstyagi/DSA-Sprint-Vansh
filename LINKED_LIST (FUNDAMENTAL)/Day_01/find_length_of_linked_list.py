# This is the geeksforgeeks question to find length of linked list
#link https://www.geeksforgeeks.org/problems/count-nodes-of-linked-list/1

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def getCount(head):
    count = 0
    current = head

    while current:
        count += 1
        current = current.next
    
    return count