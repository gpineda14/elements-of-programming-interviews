# Heaps #

A heap is a specialized complete binary tree where its keys must satisfy the heap property.

A max-heap has the property that every key at each node is at least as great as the keys stored in its children.

A min-heap is a symmetric version of the max-heap except for minimum elements.

Properties of Heaps:
- O(log n) insertions
- O(1) time for lookup of max/min element
- O(log n) deletions of max/min element

Heaps are sometimes referred to as Priority Queues because they behave like queues where each element has a priority associated with it such as max value.

## Tips for dealing with heaps ##
1. If all you care about is largest and/or smallest elements and fast lookups, deletion and search does not matter, then use a heap.
2. It is good for computing largest k or k smallest elements in a collection. Use a min-heap for largest and use max-heap for smallest.

## Python Heap Library ##
The heapq module provides us min-heap functionality.
- heapq.heapify(L)
  - transforms elements in L into a heap in-place
- heapq.nlargest(k, L)
  - returns the k largest elements in L
- heapq.nsmallest(k, L)
  - returns the k smallest elments in L
- heapq.heappush(h, e)
  - pushes a new element on the heap
- heapq.heappop(h)
  - pops the smallest element from the heap
- heapq.heappushpop(h, a)
  - pushes a on the heap and then pops and returns the smallest element
- e = h[0]
  - returns the smallest element on the heap without popping it
