def reverseKGroup(self, head, k):
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next

        n = len(arr)
        for i in range(0, n, k):
            if i + k <= n:
                arr[i:i+k] = arr[i:i+k][::-1]

        dummy = ListNode(0)
        curr = dummy
        for val in arr:
            curr.next = ListNode(val)
            curr = curr.next
    
        return dummy.next
        