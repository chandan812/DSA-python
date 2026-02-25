"""
RECURSION - Function calling itself
Base case + Recursive case
"""

def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)

def fibonacci(n):
    return n if n <= 1 else fibonacci(n - 1) + fibonacci(n - 2)

def fibonacci_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]

def power(base, exp):
    if exp == 0:
        return 1
    if exp % 2 == 0:
        half = power(base, exp // 2)
        return half * half
    return base * power(base, exp - 1)

def sum_of_digits(n):
    return 0 if n == 0 else n % 10 + sum_of_digits(n // 10)

def reverse_string(s):
    return s if len(s) <= 1 else s[-1] + reverse_string(s[:-1])

def is_palindrome(s):
    if len(s) <= 1:
        return True
    return s[0] == s[-1] and is_palindrome(s[1:-1])

def binary_search(arr, target, left, right):
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    if arr[mid] > target:
        return binary_search(arr, target, left, mid - 1)
    return binary_search(arr, target, mid + 1, right)

def tower_of_hanoi(n, source, destination, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    tower_of_hanoi(n - 1, source, auxiliary, destination)
    print(f"Move disk {n} from {source} to {destination}")
    tower_of_hanoi(n - 1, auxiliary, destination, source)

def generate_subsets(arr):
    result = []
    def backtrack(start, path):
        result.append(path[:])
        for i in range(start, len(arr)):
            path.append(arr[i])
            backtrack(i + 1, path)
            path.pop()
    backtrack(0, [])
    return result

def permutations(arr):
    if len(arr) <= 1:
        return [arr]
    result = []
    for i in range(len(arr)):
        rest = arr[:i] + arr[i+1:]
        for p in permutations(rest):
            result.append([arr[i]] + p)
    return result

if __name__ == "__main__":
    print(f"Factorial(5): {factorial(5)}")
    print(f"Fibonacci(7): {fibonacci_memo(7)}")
    print(f"Power(2, 10): {power(2, 10)}")
    print(f"Sum of digits(1234): {sum_of_digits(1234)}")
    print(f"Reverse 'hello': {reverse_string('hello')}")
    print(f"Is 'racecar' palindrome: {is_palindrome('racecar')}")
    print(f"Binary search: {binary_search([1,2,3,4,5], 3, 0, 4)}")
    print("\nTower of Hanoi:")
    tower_of_hanoi(3, 'A', 'C', 'B')
    print(f"\nSubsets of [1,2,3]: {generate_subsets([1,2,3])}")
    print(f"Permutations of [1,2,3]: {permutations([1,2,3])}")
