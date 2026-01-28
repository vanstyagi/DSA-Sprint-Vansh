def reverseList(head):
    values = []
    current = head
    while current:
        values.append(current.val)
        current = current.next

    dummy = ListNode()
    current = dummy
    for val in reversed(values):
        current.next = ListNode(val)
        current = current.next
    
    return dummy.next