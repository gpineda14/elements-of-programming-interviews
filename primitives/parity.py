# Compute Parity of word

# Bruteforce Method
# Time Complexity: O(n) where n is word size
# def parity(x):
#     result = 0
#     #terately tests value of each bit, while keeping count of 1s seen so far
#     while x:
#         result ^= x & 1
#         x >>= 1
#     return result

# Faster Method
# Time Complexity: O(k) where is number of bits
def parity(x):
    result = 0
    while x:
        result ^= 1
        x &= x - 1
    return result

# Parity Method for large numbers
def parity(x):
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    return x & 0x1
