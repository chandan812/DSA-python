"""
BIT MANIPULATION - Bitwise Operations

THEORY:
- Operations on binary representation
- Fast and space efficient
- Used in optimization and low-level programming

BITWISE OPERATORS:
- & (AND): Both bits 1 → 1
- | (OR): Any bit 1 → 1
- ^ (XOR): Different bits → 1
- ~ (NOT): Flip bits
- << (Left Shift): Multiply by 2
- >> (Right Shift): Divide by 2

COMMON TRICKS:
1. Check if power of 2: n & (n-1) == 0
2. Toggle bit: n ^ (1 << i)
3. Set bit: n | (1 << i)
4. Clear bit: n & ~(1 << i)
5. Get bit: (n >> i) & 1
6. Swap: a ^= b, b ^= a, a ^= b
7. Count set bits: Brian Kernighan's algorithm

PROPERTIES:
- a ^ a = 0
- a ^ 0 = a
- a & 0 = 0
- a | 0 = a

APPLICATIONS:
- Set operations (union, intersection)
- Subset generation
- Single number problems
- Optimization (replace *, / with shifts)
- Compression

COMMON PROBLEMS:
- Single Number
- Power of Two
- Count Set Bits
- Reverse Bits
- Subsets using bitmask
"""

def count_set_bits(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count

def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

def find_single_number(arr):
    result = 0
    for num in arr:
        result ^= num
    return result

def get_bit(n, i):
    return (n >> i) & 1

def set_bit(n, i):
    return n | (1 << i)

def clear_bit(n, i):
    return n & ~(1 << i)

def toggle_bit(n, i):
    return n ^ (1 << i)

def swap_numbers(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b

def reverse_bits(n):
    result = 0
    for i in range(32):
        result = (result << 1) | (n & 1)
        n >>= 1
    return result

def subsets_using_bits(arr):
    n = len(arr)
    result = []
    for i in range(1 << n):
        subset = []
        for j in range(n):
            if i & (1 << j):
                subset.append(arr[j])
        result.append(subset)
    return result

if __name__ == "__main__":
    print(f"Count set bits(13): {count_set_bits(13)}")
    print(f"Is power of 2(16): {is_power_of_two(16)}")
    print(f"Single number: {find_single_number([2, 3, 2, 4, 3])}")
    print(f"Get bit(5, 2): {get_bit(5, 2)}")
    print(f"Set bit(5, 1): {set_bit(5, 1)}")
    print(f"Swap(3, 5): {swap_numbers(3, 5)}")
    print(f"Subsets: {subsets_using_bits([1, 2, 3])}")
