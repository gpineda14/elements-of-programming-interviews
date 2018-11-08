# Bruteforce Method
# def dutch_flag_partition(pivot_i, A):
#     pivot = A[pivot_i]
#     # Group elements less than pivot
#     for i in range(len(A)):
#         for j in range(i + 1, len(A)):
#             if A[j] < pivot:
#                 A[i], A[j] = A[j], A[i]
#                 break
#
#     # Group elements greater than pivot
#     for i in reversed(range(len(A))):
#         if A[i] < pivot:
#             break
#         for j in reversed(range(i)):
#             if A[j] > pivot:
#                 A[i], A[j] = A[j], A[i]
#                 break

# More Efficient Method
# def dutch_flag_partition(pivot_i, A):
#     pivot = A[pivot_i]
#     smaller = 0
#     # group elements less than pivot
#     for i in range(len(A)):
#         if A[i] < pivot:
#             A[i], A[smaller] = A[smaller], A[i]
#             smaller += 1
#     # group elements greater than pivot
#     larger = len(A) - 1
#     for i in reversed(range(len(A))):
#         if A[i] < pivot:
#             break
#         elif A[i] > pivot:
#             A[i], A[larger] = A[larger], A[i]
#             larger -= 1

# Most Efficient Solution
def dutch_flag_partition(pivot_i, A):
    pivot = A[pivot_i]
    smaller = 0
    equal = 0
    larger = len(A)
    while equal < larger:
        if A[equal] < pivot:
            A[smaller], A[equal] = A[equal], A[smaller]
            smaller += 1
            equal += 1
        elif A[equal] == pivot:
            equal += 1
        else:
            larger -= 1
            A[equal], A[larger] = A[larger], A[equal]
