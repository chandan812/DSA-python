"""
SEARCHING ALGORITHMS

THEORY:
- Finding element in data structure
- Linear vs Binary search trade-offs
- Binary search requires sorted data

1. LINEAR SEARCH:
   - Check each element sequentially
   - Time: O(n)
   - Works on unsorted data
   - Simple implementation

2. BINARY SEARCH:
   - Divide and conquer on sorted data
   - Time: O(log n)
   - Requires sorted array
   - Eliminates half elements each iteration

BINARY SEARCH VARIANTS:
- First Occurrence - Find leftmost match
- Last Occurrence - Find rightmost match
- Count Occurrences - Last - First + 1
- Search in Rotated Array - Modified binary search
- Peak Element - Element greater than neighbors
- Square Root - Binary search on answer

TEMPLATE:
```
left, right = 0, n-1
while left <= right:
    mid = (left + right) // 2
    if condition:
        return mid
    elif search_left:
        right = mid - 1
    else:
        left = mid + 1
```

KEY POINTS:
- Always check mid calculation (avoid overflow)
- Decide search space reduction carefully
- Handle edge cases (empty array, single element)
"""

def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    if arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    return binary_search_recursive(arr, target, left, mid - 1)

def first_occurrence(arr, target):
    left, right = 0, len(arr) - 1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            result = mid
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result

def last_occurrence(arr, target):
    left, right = 0, len(arr) - 1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            result = mid
            left = mid + 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result

def count_occurrences(arr, target):
    first = first_occurrence(arr, target)
    if first == -1:
        return 0
    last = last_occurrence(arr, target)
    return last - first + 1

def search_rotated_array(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        if arr[left] <= arr[mid]:
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1

def find_peak_element(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] > arr[mid + 1]:
            right = mid
        else:
            left = mid + 1
    return left

def sqrt_binary_search(x):
    if x < 2:
        return x
    left, right = 1, x // 2
    while left <= right:
        mid = (left + right) // 2
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            left = mid + 1
        else:
            right = mid - 1
    return right

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(f"Linear Search: {linear_search(arr, 5)}")
    print(f"Binary Search: {binary_search(arr, 5)}")
    
    arr2 = [1, 2, 2, 2, 3, 4, 5]
    print(f"First Occurrence: {first_occurrence(arr2, 2)}")
    print(f"Last Occurrence: {last_occurrence(arr2, 2)}")
    print(f"Count Occurrences: {count_occurrences(arr2, 2)}")
    
    rotated = [4, 5, 6, 7, 0, 1, 2]
    print(f"Search Rotated: {search_rotated_array(rotated, 0)}")
    
    print(f"Peak Element: {find_peak_element([1, 2, 3, 1])}")
    print(f"Square Root: {sqrt_binary_search(16)}")
