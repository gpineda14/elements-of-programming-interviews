# Search Algorithms #

On this section, I will focus on static data that is stored in a sorted order.

When searching for an element in a sorted array, use a binary search to reduce time complexity from O(n) to O(log n).

## Tips for dealing with Binary search ##
1. They're very helpful with sorted arrays and for searching an interval of real numbers or integers
2. Look for solutions that do not require a complete sort of other computations are faster than sorting
3. Consider Time/Space tradeoffs such as making multiple passes through the data.

## Python Binary Search Libraries ##
The bisect module provides binary search functions for sorted lists.
- bisect.bisect_left(a, x)
  - returns the index of the first entry that is greater than or equal to the target value.
  - returns len(a) if all elements are less than x
- bisect.bisect_right(a, x)
  - returns index of first element that is greater than or equal to x.
  - returns len(a) if all elements are less than or equal to x.
