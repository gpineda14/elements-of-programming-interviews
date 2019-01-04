# Sorting #

Sorting is ordering a collection of items in an increasing or decreasing order. Naive sorting algorithms usually run in O(n^2) time. Other sorting algorithms such as heapsort, mergesort, and quicksort run in O(n log n) time.

A Heapsort is in-place (uses O(1) space) but is not stable (entries which are equal appear in their original order).

A mergesort is stable but is not in-place

A quicksort has a worse case run time of O(n^2).

For short arrays, you can use an insertion sort (10 or fewer elements).

## Tips for Dealing with Sorting ##

1. Time Complexity of Library sort is O(n log n) for an array with n entries and most are based on quicksort which has O(1) space complexity.
2. If you need to sort to make the next steps of an algorithm easier, you can usually use the library sort with a custom comparator.
3. If you need to design a custom sorting routine, use data structures like a BST, heap, or array indexed by values.
4. Certain problems can be easier to solve when the input is sorted.
5. For specialized input, it is possible to sort in O(n) time rather than O(n log n) such as a very small range of values or a small number of values.
6. Sometimes what to sort on is not obvious.

## Sorting Library ##

- sort() : in-place sorting, stable
  - returns None
  - takes two arguments: key=, reverse=False,True
- sorted() : sort an iterable 
