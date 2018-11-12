# Stacks #

Stacks support LIFO (Last In, First Out) for inserts and deletes. Stacks support push and pop operations, where elements are pushed to the top of the stack and the top element is popped from the stack. Stacks can be implemented using a linked list or array.

# Key Stack Operations #

- push(x)
  - add element x to the top of the stack
- pop()
  - remove top element from the stack
- peek()
  - returns top of the stack without popping it

If using a list:
- append(e)
  - add e to top of stack
- s[-1]
  - retrieve element that is at the top of the stack 
- s.pop()
  - remove and return element at top of stackk
- len(s) == 0
  - checkk if stack is empty

# Tips for dealing with Stack-related problems #

- Learn to recognize problems that can benefit from the LIFO property.
- Basic stack structures can be extracted to support additional operations such as finding max element.
