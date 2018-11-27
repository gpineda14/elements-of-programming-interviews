def search_first_of_k(A, k):
    left = 0
    right = len(A) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2
        if A[mid] > k:
            right = mid - 1
        elif A[mid] == k:
            result = mid
            right = mid - 1
        else:
            left = mid + 1

    return result
    
