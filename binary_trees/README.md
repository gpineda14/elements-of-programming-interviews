# Binary Trees #

Binary trees are either empty or a root node with a left and right binary tree as children. The root node has a value and the keys are usually stored in a sorted fashion.

If a node is a left or right child of a tree, we say it is a child of the tree.

A node is an ancestor of d if it lies on the search path from the root to d. If node is ancestor of d, we say d is a descendant of that node. A node that has no descendants except itself is called a leaf.

The depth of a node n is the number of nodes on the search path from the root to n, not including n itself. The height of a binary tree is the maximum depth of any node in that tree. A level of a tree is all nodes at the same depth. The root node of a tree has a depth of 0.

A full binary tree is a binary tree in which every node other than the leaves has two children. A perfect binary tree is a full binary tree in which all leaves are at the same depth, in which every parent has two children. A complete binary tree is a binary tree in which at every level is completely filled and all nodes are as far left as possible.

## Tips for Dealing with Binary Trees ##

1. Recursive algorithms are well-suited to problems with trees.
2. Remember to include space that is implicitly allocated on the function call stack when doing space complexity analysis.
3. Some tree problems have simple brute-force solutions that use O(n) space, but more clever solutions use the existing tree nodes to reduce space complexity to O(1).
4. Consider how left and right-skewed trees have time complexity. Balanced trees usually give us O(log n) complexity but O(n) for skewed trees.
5. Be sure not to mistake a node that has a single child as a leaf.
