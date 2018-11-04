# Primitives #

This is a program that counts the number of bits that are set to 1 in a positive integer

def count_bits(x):
  num_bits = 0
  while x:
    num_bits += x & 1
    x >>= 1
  return num_bits

It tests one bit at a time, starting with the least significant bit

Python has a number of built-in types such as:
- Numerics (integers)
- Sequences (lists)
- mapping (dict)
- classes

All instances are objects

Integers in Python 3 ae unbounded. YOu can use the constant sys.maxsize to find the word-size, which is the maximum value integer that can be stored in the word.

Bounds on floats are specified in sys.float_info

## Bitwise Manipulation ##

Bitwise Manipulation are operations that are performed on the bit level.

A byte consists of 8 bits and any number can be represented using bits in a computer.

Here are some common bitwise operations:
- Right Shift (x >> y): returns x with the bits shifted to the right by y places. This is the say as // x by 2^y
- Left Shift (x << y): returns x with the bits shifted to the left by y places. This is the same as multiplying x by 2^y.
- AND (x & y): does a bitwise and, which means each bit of the output is 1 if the corresponding bit of x and of y is 1, otherwise it's 0
- OR (x | y): does a bitwise or. Each bit of the output is 0 if the corresponding bit of x and of y is 0, otherwise its 1.
- Complement (~x): returns the complement of x, which is the number you get by switching each 1 for a 0 and each 0 for a 1. This is the same as -x-1.
- XOR (x ^ y): each bit of the output is the same as the corresponding bit in x if that bit in y is 0. and its the complement of the bit in x if that bit in y is 1.

A bit mask is a variable that aids you with bitwise operations. A bit mask can help you turn specific bits on, turn others off, or collect data from an integer.

For example, the following program checks to see if the forth bit from the right is on, using a mask

def check_bit4(input):
  mask=0b1000
  if input & mask > 0:
    return "on"
  else:
    return "off"

## Clear least significant bit ##

def clearLowestBit(n):
  return n & (n - 1)

## Useful Methods ##

- abs(n): return absolute value of n
- math.ceil(n): rounds n up to nearest int
- math.floor(n): rounds n down to nearest int
- min(a, b): returns the min between a and b. can be used with arrays as well
- max(a, b): returns the max between a and b. can be used with arrays as well.
- pow(x, y): returns x to the power y
- math.sqrt(n): returns square root of n
- str(int): converts int to string
- int(str): converts string to int
- float(str): converts string to float. you can use float(inf) to create pseudo max-int/min-int
