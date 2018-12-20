def plus_one(A):
    # Add 1 to the last value of array
    A[-1] += 1
    # iterate through the array in reverse
    for i in reversed(range(1, len(A))):
        # if A[i] is not 10, we are done carrying over, so break
        if A[i] != 10:
            break
        # else we carry the value by setting A[i] to 0
        # and add 1 to its previous value
        A[i] = 0
        A[i - 1] += 1

    # if first value is 10, then we final carry
    # by setting A[0] to 1 and appending 0 to the end
    if A[0] == 10:
        A[0] = 1
        A.append(0)

    return A
