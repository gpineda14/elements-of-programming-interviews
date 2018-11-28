# Binary Search Trees #

Binary Search Trees is a very versatile data structure. It allows you to efficiently search keys, find min, find max, look for successor or predecessor of key, and enumerate keys in a range in sorted order.

BSTs store their keys in a sorted order but allow for me efficient addition and deletions than arrays. The keys stored at nodes must also respect the BST property. If implemented correctly, insertions and deletions of keys in a tree have a time complexity of O(log n).

BSTs are very useful for searching as they offer fast lookups, give you the ability to find min and max elements, and find the next largest/next smallest element in O(log n) time. Like hash maps, they require O(n) space.

## Tips for dealing with Binary Search Trees ##

1. BSTs can iterate through elements in a sorted order in O(n) time.
2. Some problems require a combination of BSTs and hash tables.
3. The BST property is a global property that must be satisfied at all levels of the tree
4. Sometimes its necessary to augment the BST to make it possible to manipulate more complicated data.

## Python BST Libraries ##

We can use bintrees for BST library support
- insert(e)
  - insert element e in the BST
- discard(e)
  - remove element e in the BST
- min_item()
  - return smallest key-value pair in BST
- max_item()
  - return largest key-value pair in BST
- min_key()
  - return smallest key in BST
- max_key()
  - return largest key in BST
- pop_min()
  - remove and return smallest key-value pair in BST
- pop_max()
  - remove and return largest key-value pair in BST 
