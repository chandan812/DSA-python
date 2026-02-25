"""
STRING ALGORITHMS - Pattern Matching
"""

def kmp_search(text, pattern):
    def compute_lps(pattern):
        lps = [0] * len(pattern)
        length = 0
        i = 1
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps
    
    lps = compute_lps(pattern)
    result = []
    i = j = 0
    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == len(pattern):
            result.append(i - j)
            j = lps[j - 1]
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return result

def rabin_karp(text, pattern):
    d = 256
    q = 101
    m = len(pattern)
    n = len(text)
    p = t = 0
    h = pow(d, m - 1) % q
    result = []
    
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q
    
    for i in range(n - m + 1):
        if p == t:
            if text[i:i + m] == pattern:
                result.append(i)
        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            if t < 0:
                t += q
    return result

def z_algorithm(s):
    n = len(s)
    z = [0] * n
    l = r = 0
    for i in range(1, n):
        if i > r:
            l = r = i
            while r < n and s[r - l] == s[r]:
                r += 1
            z[i] = r - l
            r -= 1
        else:
            k = i - l
            if z[k] < r - i + 1:
                z[i] = z[k]
            else:
                l = i
                while r < n and s[r - l] == s[r]:
                    r += 1
                z[i] = r - l
                r -= 1
    return z

def manacher_algorithm(s):
    t = '#'.join('^{}$'.format(s))
    n = len(t)
    p = [0] * n
    c = r = 0
    for i in range(1, n - 1):
        p[i] = (r > i) and min(r - i, p[2 * c - i])
        while t[i + 1 + p[i]] == t[i - 1 - p[i]]:
            p[i] += 1
        if i + p[i] > r:
            c, r = i, i + p[i]
    max_len, center = max((n, i) for i, n in enumerate(p))
    return s[(center - max_len) // 2:(center + max_len) // 2]

if __name__ == "__main__":
    text = "ababcabcabababd"
    pattern = "ababd"
    print(f"KMP Search: {kmp_search(text, pattern)}")
    print(f"Rabin-Karp: {rabin_karp(text, pattern)}")
    print(f"Z-Algorithm: {z_algorithm('aabxaabxcaabxaabxay')}")
    print(f"Longest Palindrome: {manacher_algorithm('babad')}")
