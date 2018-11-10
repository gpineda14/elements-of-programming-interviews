# Linked Lists #

A linked list is a data structure that contains a sequence of nodes such that each node contains the object and a reference to the next node on the list.

We refer to the first node as the head and the last node as a tail. There are also variants of linked lists such as the doubly linked list which has a reference to its predecessor node as well as the next node. There is also a sentinel node/self-loop that can be used instead of null to mark the end of the list.

Properties of Linked Lists:
- insertion and deletion of elements is O(1)
- finding kth element is O(k)

## Tips for Dealing with Linked Lists ##

1. Like arrays and strings, they usually have a brute-force solution that uses O(n) space but can be reduced to O(1) by using the existing list nodes 
2. Focus on what is specified by the problem
3. Don't forget to continuously update the linked list
4. Use the two iterators, slow and fast, while working with singly linked lists
