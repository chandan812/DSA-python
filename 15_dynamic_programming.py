"""
DYNAMIC PROGRAMMING - Optimization Technique

THEORY:
- Solve complex problems by breaking into subproblems
- Store results to avoid recomputation
- Optimal substructure + Overlapping subproblems

APPROACHES:
1. Memoization (Top-Down):
   - Recursion + Cache
   - Solve as needed
   - Natural to write

2. Tabulation (Bottom-Up):
   - Iterative + Table
   - Solve all subproblems
   - Better space optimization

STEPS TO SOLVE:
1. Define state (dp[i] represents what?)
2. Find recurrence relation
3. Identify base cases
4. Determine computation order
5. Optimize space if possible

COMMON PATTERNS:
1. Linear DP - Fibonacci, Climbing Stairs
2. 2D DP - LCS, Edit Distance, Knapsack
3. String DP - Palindrome, Pattern Matching
4. Tree DP - Diameter, Path Sum
5. Bitmask DP - Subset problems

OPTIMIZATION:
- Space: Often reduce from 2D to 1D
- Time: Memoization avoids redundant calls

KEY PROBLEMS:
- Fibonacci, Climbing Stairs
- Coin Change, Knapsack
- LCS, LIS, Edit Distance
- Matrix Chain Multiplication
- Subset Sum, Partition
"""

def fibonacci_dp(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

def climbing_stairs(n):
    if n <= 2:
        return n
    dp = [0] * (n + 1)
    dp[1], dp[2] = 1, 2
    for i in range(3, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1

def longest_increasing_subsequence(arr):
    if not arr:
        return 0
    dp = [1] * len(arr)
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

def longest_common_subsequence(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n]

def knapsack_01(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], values[i-1] + dp[i-1][w - weights[i-1]])
            else:
                dp[i][w] = dp[i-1][w]
    return dp[n][capacity]

def edit_distance(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    return dp[m][n]

def max_subarray_sum(arr):
    max_sum = curr_sum = arr[0]
    for num in arr[1:]:
        curr_sum = max(num, curr_sum + num)
        max_sum = max(max_sum, curr_sum)
    return max_sum

def house_robber(arr):
    if not arr:
        return 0
    if len(arr) == 1:
        return arr[0]
    dp = [0] * len(arr)
    dp[0], dp[1] = arr[0], max(arr[0], arr[1])
    for i in range(2, len(arr)):
        dp[i] = max(dp[i-1], arr[i] + dp[i-2])
    return dp[-1]

if __name__ == "__main__":
    print(f"Fibonacci(10): {fibonacci_dp(10)}")
    print(f"Climbing Stairs(5): {climbing_stairs(5)}")
    print(f"Coin Change: {coin_change([1, 2, 5], 11)}")
    print(f"LIS: {longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18])}")
    print(f"LCS: {longest_common_subsequence('abcde', 'ace')}")
    print(f"Knapsack: {knapsack_01([1, 2, 3], [6, 10, 12], 5)}")
    print(f"Edit Distance: {edit_distance('horse', 'ros')}")
    print(f"Max Subarray: {max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4])}")
    print(f"House Robber: {house_robber([2, 7, 9, 3, 1])}")
