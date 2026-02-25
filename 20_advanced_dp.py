"""
ADVANCED DYNAMIC PROGRAMMING
"""

def matrix_chain_multiplication(dims):
    n = len(dims) - 1
    dp = [[0] * n for _ in range(n)]
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                cost = dp[i][k] + dp[k+1][j] + dims[i] * dims[k+1] * dims[j+1]
                dp[i][j] = min(dp[i][j], cost)
    return dp[0][n-1]

def egg_drop(eggs, floors):
    dp = [[0] * (floors + 1) for _ in range(eggs + 1)]
    for i in range(1, eggs + 1):
        dp[i][1] = 1
    for j in range(1, floors + 1):
        dp[1][j] = j
    for i in range(2, eggs + 1):
        for j in range(2, floors + 1):
            dp[i][j] = float('inf')
            for k in range(1, j + 1):
                dp[i][j] = min(dp[i][j], 1 + max(dp[i-1][k-1], dp[i][j-k]))
    return dp[eggs][floors]

def partition_equal_subset(arr):
    total = sum(arr)
    if total % 2:
        return False
    target = total // 2
    dp = [False] * (target + 1)
    dp[0] = True
    for num in arr:
        for i in range(target, num - 1, -1):
            dp[i] = dp[i] or dp[i - num]
    return dp[target]

def word_break(s, wordDict):
    dp = [False] * (len(s) + 1)
    dp[0] = True
    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in wordDict:
                dp[i] = True
                break
    return dp[len(s)]

def palindrome_partitioning(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = True
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                dp[i][j] = (length == 2) or dp[i+1][j-1]
    cuts = [0] * n
    for i in range(n):
        if dp[0][i]:
            cuts[i] = 0
        else:
            cuts[i] = float('inf')
            for j in range(i):
                if dp[j+1][i]:
                    cuts[i] = min(cuts[i], cuts[j] + 1)
    return cuts[n-1]

def longest_palindromic_subsequence(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
    return dp[0][n-1]

if __name__ == "__main__":
    print(f"Matrix Chain: {matrix_chain_multiplication([10, 20, 30, 40, 30])}")
    print(f"Egg Drop: {egg_drop(2, 10)}")
    print(f"Partition Equal: {partition_equal_subset([1, 5, 11, 5])}")
    print(f"Word Break: {word_break('leetcode', {'leet', 'code'})}")
    print(f"Palindrome Partition: {palindrome_partitioning('aab')}")
    print(f"Longest Palindromic Subseq: {longest_palindromic_subsequence('bbbab')}")
