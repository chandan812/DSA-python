"""
ARRAYS - Foundation of DSA
Time Complexity: Access O(1), Search O(n), Insert/Delete O(n)
"""

def reverse_array(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

def rotate_array(arr, k):
    n = len(arr)
    k = k % n
    return arr[-k:] + arr[:-k]

def max_subarray_sum(arr):
    max_sum = current_sum = arr[0]
    for num in arr[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum

def two_sum(arr, target):
    seen = {}
    for i, num in enumerate(arr):
        if target - num in seen:
            return [seen[target - num], i]
        seen[num] = i
    return []

def remove_duplicates(arr):
    if not arr:
        return 0
    j = 0
    for i in range(1, len(arr)):
        if arr[i] != arr[j]:
            j += 1
            arr[j] = arr[i]
    return j + 1

def merge_sorted(arr1, arr2):
    result = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    result.extend(arr1[i:])
    result.extend(arr2[j:])
    return result

def find_missing(arr, n):
    return n * (n + 1) // 2 - sum(arr)

def find_leaders(arr):
    leaders = []
    max_right = float('-inf')
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] > max_right:
            leaders.append(arr[i])
            max_right = arr[i]
    return leaders[::-1]

if __name__ == "__main__":
    print("=== REVERSE ===")
    print(reverse_array([1, 2, 3, 4, 5]))
    
    print("\n=== ROTATE ===")
    print(rotate_array([1, 2, 3, 4, 5], 2))
    
    print("\n=== MAX SUBARRAY SUM ===")
    print(max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    
    print("\n=== TWO SUM ===")
    print(two_sum([2, 7, 11, 15], 9))
    
    print("\n=== MERGE SORTED ===")
    print(merge_sorted([1, 3, 5], [2, 4, 6]))
    
    print("\n=== MISSING NUMBER ===")
    print(find_missing([1, 2, 4, 5], 5))
    
    print("\n=== LEADERS ===")
    print(find_leaders([16, 17, 4, 3, 5, 2]))
