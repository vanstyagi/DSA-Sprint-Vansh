def getIntersectionNode(headA, headB):
    def get_length(head):
        length = 0
        while head:
            length += 1
            head = head.next
        return length

    lenA, lenB = get_length(headA), get_length(headB)

    currentA, currentB = headA, headB
    if lenA > lenB:
        for _ in range(lenA - lenB):
            currentA = currentA.next
    elif lenB > lenA:
        for _ in range(lenB - lenA):
            currentB = currentB.next

    while currentA and currentB:
        if currentA is currentB:  
            return currentA
        currentA = currentA.next
        currentB = currentB.next
    
    return None