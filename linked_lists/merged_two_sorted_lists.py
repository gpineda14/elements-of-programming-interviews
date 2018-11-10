def merge_two_sorted_lists(l1, l2):
    list = ListNode()
    curr = list

    while l1 and l2:
        if l1.data < l2.data:
            curr.next = l1
            l1.next
        else:
            curr.next = l2.data
            l2.next
        curr = curr.next

    curr.next = l1 or l2
    return list.next
    
