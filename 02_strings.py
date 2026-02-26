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

def reverse_string(s):
    return s[::-1]

def is_palindrome(s):
    return s == s[::-1]

def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

def first_non_repeating(s):
    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1
    for char in s:
        if count[char] == 1:
            return char
    return None

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

def valid_parentheses(s):
    stack = []
    pairs = {'(': ')', '{': '}', '[': ']'}
    for char in s:
        if char in pairs:
            stack.append(char)
        elif not stack or pairs[stack.pop()] != char:
            return False
    return len(stack) == 0

def reverse_words(s):
    return ' '.join(s.split()[::-1])

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
