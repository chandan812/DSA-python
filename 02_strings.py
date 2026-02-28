"""
STRINGS - Character Array Manipulation

THEORY:
- Sequence of characters stored as array
- Immutable in Python (creates new string on modification)
- Can be indexed, sliced like arrays
- Common operations: concatenation, substring, pattern matching

TIME COMPLEXITY:
- Access: O(1)
- Concatenation: O(n+m)
- Substring: O(k) where k is substring length
- Search: O(n*m) naive, O(n+m) with KMP

COMMON TECHNIQUES:
1. Two Pointers - Palindrome check, reverse
2. Sliding Window - Longest substring problems
3. Hashing - Anagram detection, character frequency
4. Pattern Matching - KMP, Rabin-Karp algorithms

IMPORTANT PATTERNS:
- Palindrome: Same forwards and backwards
- Anagram: Same characters, different order
- Subsequence: Characters in same order, not necessarily contiguous
- Substring: Contiguous sequence of characters
"""

# Reverse string using slicing
# Time: O(n), Space: O(n)
def reverse_string(s):
    return s[::-1]

# Check if string is palindrome
# Time: O(n), Space: O(n)
def is_palindrome(s):
    return s == s[::-1]

# Check if two strings are anagrams
# Time: O(n log n), Space: O(n)
def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

# Find first non-repeating character
# Time: O(n), Space: O(n)
def first_non_repeating(s):
    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1
    for char in s:
        if count[char] == 1:
            return char
    return None

# Longest substring without repeating characters
# Time: O(n), Space: O(min(n, charset_size))
# Uses sliding window technique
def longest_unique_substring(s):
    char_set = set()
    left = max_len = 0
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)
    return max_len

# String compression (e.g., "aabccc" -> "a2b1c3")
# Time: O(n), Space: O(n)
def compress_string(s):
    if not s:
        return ""
    result = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            result.append(s[i-1] + str(count))
            count = 1
    result.append(s[-1] + str(count))
    compressed = ''.join(result)
    return compressed if len(compressed) < len(s) else s

# Check if parentheses are balanced
# Time: O(n), Space: O(n)
def valid_parentheses(s):
    stack = []
    pairs = {'(': ')', '{': '}', '[': ']'}
    for char in s:
        if char in pairs:
            stack.append(char)
        elif not stack or pairs[stack.pop()] != char:
            return False
    return len(stack) == 0

# Reverse words in a string
# Time: O(n), Space: O(n)
def reverse_words(s):
    return ' '.join(s.split()[::-1])

# Find longest common prefix among strings
# Time: O(S) where S is sum of all characters, Space: O(1)
def longest_common_prefix(strs):
    if not strs:
        return ""
    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix

if __name__ == "__main__":
    print(f"Reverse: {reverse_string('hello')}")
    print(f"Palindrome: {is_palindrome('racecar')}")
    print(f"Anagram: {is_anagram('listen', 'silent')}")
    print(f"First Non-Repeating: {first_non_repeating('leetcode')}")
    print(f"Longest Unique: {longest_unique_substring('abcabcbb')}")
    print(f"Compress: {compress_string('aabcccccaaa')}")
    print(f"Valid Parentheses: {valid_parentheses('()[]{}')}")
    print(f"Reverse Words: {reverse_words('the sky is blue')}")
    print(f"Common Prefix: {longest_common_prefix(['flower', 'flow', 'flight'])}")
