"""
MATH ALGORITHMS - Number Theory

THEORY:

1. GCD (Greatest Common Divisor):
   - Euclidean Algorithm: O(log min(a,b))
   - gcd(a,b) = gcd(b, a%b)

2. LCM (Least Common Multiple):
   - lcm(a,b) = (a*b) / gcd(a,b)

3. PRIME NUMBERS:
   - Only divisible by 1 and itself
   - Trial Division: O(√n)
   - Sieve of Eratosthenes: O(n log log n)

4. PRIME FACTORIZATION:
   - Express n as product of primes
   - Time: O(√n)

5. MODULAR ARITHMETIC:
   - (a+b) % m = ((a%m) + (b%m)) % m
   - (a*b) % m = ((a%m) * (b%m)) % m
   - Fast exponentiation: O(log n)

6. COMBINATORICS:
   - nCr = n! / (r! * (n-r)!)
   - Pascal's Triangle for small values

APPLICATIONS:
- Cryptography (RSA)
- Hashing
- Random number generation
- Competitive programming

COMMON PROBLEMS:
- Prime checking
- Prime factorization
- GCD/LCM
- Modular exponentiation
- Fibonacci (Matrix method)
- Factorial
- Combinations/Permutations
"""

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return [i for i in range(n + 1) if primes[i]]

def prime_factors(n):
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors

def power_mod(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp = exp >> 1
        base = (base * base) % mod
    return result

def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)

def nCr(n, r):
    if r > n:
        return 0
    if r == 0 or r == n:
        return 1
    return nCr(n - 1, r - 1) + nCr(n - 1, r)

def fibonacci_matrix(n):
    def matrix_mult(A, B):
        return [[A[0][0]*B[0][0] + A[0][1]*B[1][0], A[0][0]*B[0][1] + A[0][1]*B[1][1]],
                [A[1][0]*B[0][0] + A[1][1]*B[1][0], A[1][0]*B[0][1] + A[1][1]*B[1][1]]]
    
    def matrix_power(M, n):
        if n == 1:
            return M
        if n % 2 == 0:
            half = matrix_power(M, n // 2)
            return matrix_mult(half, half)
        return matrix_mult(M, matrix_power(M, n - 1))
    
    if n <= 1:
        return n
    M = [[1, 1], [1, 0]]
    result = matrix_power(M, n)
    return result[0][1]

if __name__ == "__main__":
    print(f"GCD(48, 18): {gcd(48, 18)}")
    print(f"LCM(12, 15): {lcm(12, 15)}")
    print(f"Is 17 prime: {is_prime(17)}")
    print(f"Primes up to 30: {sieve_of_eratosthenes(30)}")
    print(f"Prime factors of 60: {prime_factors(60)}")
    print(f"Power mod (2^10 mod 1000): {power_mod(2, 10, 1000)}")
    print(f"Factorial(5): {factorial(5)}")
    print(f"C(5, 2): {nCr(5, 2)}")
    print(f"Fibonacci(10): {fibonacci_matrix(10)}")
