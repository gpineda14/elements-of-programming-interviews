def reverse_sublist(L, s, f):
    dummy_head = ListNode(0)
    dummy_head.next = L
    sublist_head = dummy_head

    for _ in range(1, s):
        sublist_head = sublist_head.next

    sublist_iter = sublist_head.next
    for _ in range(f - s):
        temp = sublist_iter.next
        sublist_iter.next = temp.next
        temp.next = sublist_head.next
        sublist_head.next = temp

    return dummy_head
    # time complexity: O(f)
