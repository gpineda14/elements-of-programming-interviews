# Queues #

Queues support two basic operations, enqueue and dequeue. Elements are added with enqueue and removed with dequeue. Queues follow the FIFO (First In, First Out) structure. Most recently inserted element is referred to as the tail or back element. Queues can also be implemented using a linked list or array. A deque is a double-ended queue, which is a linked list in which all insertions and deletions are from one of the two ends of the list. An insertion to the front is called a push and an insertion to the back is called an inject. A deletion from the front is called a pop and deletion from the back is called an eject.

## Tips for dealing with Queues ##

1. Learn to recognize when the FIFO property is applicable.
2. Use collections.deque when you don't have to create your own Queue class for queues
