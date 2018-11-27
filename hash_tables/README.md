# Hash Tables #

Hash tables are data structures that are used to store keys with corresponding values. Hash tables have insertions, deletions, and lookups running in O(1) time.

A hash table is good for representing a dictionary (a set of strings). They are good when you need to store a set of strings.

## Tips for dealing with Hash Tables ##
1. Hash Tables have the best performance for lookups, insertions, and deletions which is O(1)
2. Use hash code as signature to enhance performance

## Python Hash Table Libraries ##
There are many hash table-based data structures in Python such as set, dict, collections.defaultdict, and collections.Counter.
- Sets simply store keys where the others store key-value pairs.
- Searching for a key that is not in dict leads to a KeyError exception
- collections.defaultdict returns default value when key is not found in collections.defaultdict
- collections.Counter is used for counting number of occurrences of keys.

### Sets ###
- s.add(x)
  - add x to set s
- s.remove(x)
  - remove x from set s
- x in s
  - check if x is in s
- s <= t
  - checks if s is a subset of t
- s - t
  - returns elements that are in s but not in t

### collections.Counter ###
- c = collections.Counter(a=3, b=1)
  - instantiate a counter class
- c + d
  - add values of two counters that have equal keys together
- c - d
  - subtract values of two counters that have equals keys

### Dict, collections.defaultdict, collections.Collections ###
- iterator.items()
  - iterate over key-value pairs
- iterator.values()
  - iterate over values
