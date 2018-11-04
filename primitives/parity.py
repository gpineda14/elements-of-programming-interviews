# Compute Parity of word
# Bruteforce Method
def parity(x):
    result = 0
    while x:
        result ^= x & 1
        x >>= 1
    return result
    
