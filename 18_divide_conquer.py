"""
DIVIDE AND CONQUER - Break into subproblems

THEORY:
- Break problem into smaller subproblems
- Solve subproblems recursively
- Combine solutions

STEPS:
1. Divide - Break into smaller subproblems
2. Conquer - Solve subproblems recursively
3. Combine - Merge solutions

TIME COMPLEXITY:
Master Theorem: T(n) = aT(n/b) + f(n)
- a = number of subproblems
- b = factor by which size reduces
- f(n) = cost of divide and combine

COMMON ALGORITHMS:
1. Merge Sort - T(n) = 2T(n/2) + O(n) = O(n log n)
2. Quick Sort - T(n) = 2T(n/2) + O(n) = O(n log n) avg
3. Binary Search - T(n) = T(n/2) + O(1) = O(log n)
4. Strassen's Matrix - O(n^2.807)
5. Karatsuba Multiplication - O(n^1.585)

DIVIDE & CONQUER vs DP:
- D&C: Independent subproblems
- DP: Overlapping subproblems

ADVANTAGES:
- Efficient algorithms
- Parallelizable
- Cache-friendly

COMMON PROBLEMS:
- Sorting (Merge, Quick)
- Binary Search
- Maximum Subarray
- Closest Pair of Points
- Count Inversions
"""

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def binary_search(arr, target, left, right):
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    if arr[mid] > target:
        return binary_search(arr, target, left, mid - 1)
    return binary_search(arr, target, mid + 1, right)

def max_subarray_divide_conquer(arr, left, right):
    if left == right:
        return arr[left]
    mid = (left + right) // 2
    left_max = max_subarray_divide_conquer(arr, left, mid)
    right_max = max_subarray_divide_conquer(arr, mid + 1, right)
    cross_max = max_crossing_sum(arr, left, mid, right)
    return max(left_max, right_max, cross_max)

def max_crossing_sum(arr, left, mid, right):
    left_sum = float('-inf')
    curr_sum = 0
    for i in range(mid, left - 1, -1):
        curr_sum += arr[i]
        left_sum = max(left_sum, curr_sum)
    right_sum = float('-inf')
    curr_sum = 0
    for i in range(mid + 1, right + 1):
        curr_sum += arr[i]
        right_sum = max(right_sum, curr_sum)
    return left_sum + right_sum

def count_inversions(arr):
    if len(arr) <= 1:
        return arr, 0
    mid = len(arr) // 2
    left, left_inv = count_inversions(arr[:mid])
    right, right_inv = count_inversions(arr[mid:])
    merged, split_inv = merge_count(left, right)
    return merged, left_inv + right_inv + split_inv

def merge_count(left, right):
    result = []
    inversions = 0
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            inversions += len(left) - i
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result, inversions

if __name__ == "__main__":
    arr = [38, 27, 43, 3, 9, 82, 10]
    print(f"Merge Sort: {merge_sort(arr.copy())}")
    print(f"Quick Sort: {quick_sort(arr.copy())}")
    print(f"Binary Search: {binary_search([1, 2, 3, 4, 5], 3, 0, 4)}")
    print(f"Max Subarray: {max_subarray_divide_conquer([-2, 1, -3, 4, -1, 2, 1], 0, 6)}")
    print(f"Count Inversions: {count_inversions([2, 4, 1, 3, 5])[1]}")
