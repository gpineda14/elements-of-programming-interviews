def search_list(l, key):
    while l and l.data != key:
        l = l.next
    return l
