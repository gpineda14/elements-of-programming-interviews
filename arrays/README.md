# Arrays #

Arrays are data structures that are contiguous blocks of memory. Its used to represent sequences where A[i] denotes the (i + 1)th object stored in the array.

Properties of Array:
- Retrieval and updating elements takes O(1) time.
- Insertion into full array can take O(n) time.
- Can reduce insertion time by making new array a constant factor larger than original array
- Deletion can take O(n - i) where i is the index of the deleted element.

## Tips with dealing with Arrays ##

1. Try to use the array itself when writing solutions to reduce space complexity to O(1)
2. Write values to array from the back
3. Instead of deleting an array, overwrite it instead
4. Be careful not to make off-by-1 errors
5. Don't worry about preserving integrity of array until it's time to return
6. Arrays are good when you know something about the distribution of elements in advance
7. Consider processing digits from the back of the array when dealing with integers encoded by array. You can reverse the array to do this.
8. Use parallel logic for rows and for columns
9. Simulate the specifications by computing output from the beginning.

## Key Array/List Methods ##

- Instantiating Arrays:
  - [3, 5, 6, 7, 8]
  - [1] + [0] * 10 => [1,0,0,0,0,0,0,0,0,0,0]
  - list(range(100)) => [0 ... 99]
- Get Size of Array:
  - len(A)
- Add to Back of Array:
  - A.append(5)
- Remove Element from Array:
  - A.remove(elem)
- Insert Element at Position i in Array:
  - A.insert(i, elem)
- Instantiating 2D Arrays:
  - [[1,2,4], [3,5,7,9], [13]]
  - [[0] * 10] * 10=> Array with 10 rows and 10 columns
- Presence of element in Array:
  - elem in A
- Make reference to Array:
  - B = A
- Make Copy of Array:
  - B = list(A)
  - B = A[:]
- Delete ith Element:
  - del A[i]
  - del A[i:j], removes elements i to j - 1
- Find min and max of Array:
  - min(A)
  - max(A)
- Binary Search for Sorted Arrays:
  - bisect.bisect(A, 6)
  - bisect.bisect_left(A, 6)
  - bisect.bisect_right(A, 6)
- Reverse Array:
  - A.reverse() (in-place)
  - reversed(A) (returns iterator)
- Sort Array:
  - A.sort() (in-place)
  - sorted(A) (returns a copy)
- Rotate Array by k to the left:
  - A[k:] + A[:k]
- Use list comprehensions
  - [x ** 2 for x in range(6)] => [0, 1, 4, 9, 16, 25]
  - [x ** 2 for x in range(6) if x % 2 == 0] => [0, 4, 16]
  - Avoid more than two nested comprehensions
