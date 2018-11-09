# Strings #

Strings can be viewed as a special kind of array made of characters with the exception of certain operations specific to strings.

## Key tips when dealing with strings ##

1. Most string problems have a brute-force solution that requires O(n) space, but can improved on to reduce space complexity to O(1).
2. Understand that strings are immutable, so know alternatives to immutable strings if concatenation is required.

## Key String Operations ##

- lookup at index i
  - s[i]
- find length of string
  - len(s)
- concatenation of s and t
  - s + t
- return slice of string from i to n - 1
  - s[i:n]
- check if char is in string
  - c in s
- Remove whitespace before and after characters in string
  - s.strip()
- Check if string starts with char:
  - s.startswith(char)
- Check if string ends with char:
  - s.endswith(char)
- Convert string to array by splitting with delimiter n
  - s.split(n)
- join array or tuple together separated by n
  - n.join(arr)
- convert uppercase letters to lowercase
  - s.tolower()
- convert lowercase letters to uppercase
  - s.upper()
