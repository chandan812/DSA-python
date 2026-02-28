# DSA FUNCTION REFERENCE GUIDE

## This file contains explanations for all functions across all 24 files

### 01_arrays.py
- reverse_array(arr): Reverse array in-place using two pointers | Time: O(n), Space: O(1)
- rotate_array(arr, k): Rotate array right by k positions | Time: O(n), Space: O(n)
- max_subarray_sum(arr): Kadane's Algorithm for max subarray sum | Time: O(n), Space: O(1)
- two_sum(arr, target): Find two indices that sum to target using hash map | Time: O(n), Space: O(n)
- remove_duplicates(arr): Remove duplicates from sorted array in-place | Time: O(n), Space: O(1)
- merge_sorted(arr1, arr2): Merge two sorted arrays | Time: O(m+n), Space: O(m+n)
- find_missing(arr, n): Find missing number using sum formula | Time: O(n), Space: O(1)
- find_leaders(arr): Find elements greater than all to right | Time: O(n), Space: O(n)

### 02_strings.py
- reverse_string(s): Reverse using slicing | Time: O(n), Space: O(n)
- is_palindrome(s): Check if palindrome | Time: O(n), Space: O(n)
- is_anagram(s1, s2): Check if anagrams by sorting | Time: O(n log n), Space: O(n)
- first_non_repeating(s): Find first non-repeating char | Time: O(n), Space: O(n)
- longest_unique_substring(s): Sliding window for longest unique substring | Time: O(n), Space: O(min(n, charset))
- compress_string(s): Compress consecutive chars | Time: O(n), Space: O(n)
- valid_parentheses(s): Check balanced parentheses using stack | Time: O(n), Space: O(n)
- reverse_words(s): Reverse word order | Time: O(n), Space: O(n)
- longest_common_prefix(strs): Find longest common prefix | Time: O(S), Space: O(1)

### 03_linked_lists.py
LinkedList methods:
- insert_at_end(data): Insert at end | Time: O(n), Space: O(1)
- insert_at_beginning(data): Insert at beginning | Time: O(1), Space: O(1)
- delete_node(key): Delete node with key | Time: O(n), Space: O(1)
- display(): Display as string | Time: O(n), Space: O(n)
- reverse(): Reverse in-place | Time: O(n), Space: O(1)
- detect_cycle(): Floyd's cycle detection | Time: O(n), Space: O(1)
- find_middle(): Find middle using fast/slow pointers | Time: O(n), Space: O(1)

### 04_stacks.py
- Stack.push(item): Push to top | Time: O(1), Space: O(1)
- Stack.pop(): Pop from top | Time: O(1), Space: O(1)
- Stack.peek(): View top | Time: O(1), Space: O(1)
- is_balanced(expression): Check balanced parentheses | Time: O(n), Space: O(n)
- next_greater_element(arr): Find next greater for each | Time: O(n), Space: O(n)
- evaluate_postfix(expression): Evaluate postfix | Time: O(n), Space: O(n)
- MinStack.get_min(): Get minimum in O(1) | Time: O(1), Space: O(1)

### 05_queues.py
- Queue.enqueue(item): Add to rear | Time: O(1), Space: O(1)
- Queue.dequeue(): Remove from front | Time: O(1), Space: O(1)
- CircularQueue: Fixed size circular queue
- reverse_queue(q): Reverse using stack | Time: O(n), Space: O(n)
- first_non_repeating_stream(stream): First non-repeating in stream | Time: O(n), Space: O(n)

### 06_hashing.py
- HashTable.insert(key, value): Insert key-value | Time: O(1) avg, Space: O(1)
- HashTable.get(key): Get value by key | Time: O(1) avg, Space: O(1)
- two_sum(arr, target): Find pair using hash | Time: O(n), Space: O(n)
- subarray_sum_zero(arr): Check if subarray sums to 0 | Time: O(n), Space: O(n)
- longest_subarray_sum_k(arr, k): Longest subarray with sum k | Time: O(n), Space: O(n)
- count_distinct_elements(arr): Count unique elements | Time: O(n), Space: O(n)
- find_duplicates(arr): Find duplicate elements | Time: O(n), Space: O(n)

### 07_recursion.py
- factorial(n): Factorial using recursion | Time: O(n), Space: O(n)
- fibonacci(n): Fibonacci recursive | Time: O(2^n), Space: O(n)
- fibonacci_memo(n): Fibonacci with memoization | Time: O(n), Space: O(n)
- power(base, exp): Fast exponentiation | Time: O(log n), Space: O(log n)
- sum_of_digits(n): Sum digits recursively | Time: O(log n), Space: O(log n)
- reverse_string(s): Reverse recursively | Time: O(n), Space: O(n)
- is_palindrome(s): Check palindrome recursively | Time: O(n), Space: O(n)
- tower_of_hanoi(n, src, dest, aux): Solve Tower of Hanoi | Time: O(2^n), Space: O(n)
- generate_subsets(arr): Generate all subsets | Time: O(2^n), Space: O(n)
- permutations(arr): Generate all permutations | Time: O(n!), Space: O(n)

### 08_sorting.py
- bubble_sort(arr): Bubble sort | Time: O(n²), Space: O(1)
- selection_sort(arr): Selection sort | Time: O(n²), Space: O(1)
- insertion_sort(arr): Insertion sort | Time: O(n²), Space: O(1)
- merge_sort(arr): Merge sort | Time: O(n log n), Space: O(n)
- quick_sort(arr): Quick sort | Time: O(n log n) avg, Space: O(log n)
- heap_sort(arr): Heap sort | Time: O(n log n), Space: O(1)
- counting_sort(arr): Counting sort | Time: O(n+k), Space: O(k)

### 09_searching.py
- linear_search(arr, target): Linear search | Time: O(n), Space: O(1)
- binary_search(arr, target): Binary search | Time: O(log n), Space: O(1)
- first_occurrence(arr, target): First occurrence | Time: O(log n), Space: O(1)
- last_occurrence(arr, target): Last occurrence | Time: O(log n), Space: O(1)
- count_occurrences(arr, target): Count occurrences | Time: O(log n), Space: O(1)
- search_rotated_array(arr, target): Search in rotated array | Time: O(log n), Space: O(1)
- find_peak_element(arr): Find peak element | Time: O(log n), Space: O(1)
- sqrt_binary_search(x): Square root using binary search | Time: O(log x), Space: O(1)

### 10_trees.py
BinaryTree methods:
- inorder(node): Inorder traversal | Time: O(n), Space: O(h)
- preorder(node): Preorder traversal | Time: O(n), Space: O(h)
- postorder(node): Postorder traversal | Time: O(n), Space: O(h)
- level_order(root): Level order (BFS) | Time: O(n), Space: O(w)
- height(node): Tree height | Time: O(n), Space: O(h)

BST methods:
- insert(val): Insert in BST | Time: O(h), Space: O(h)
- search(val): Search in BST | Time: O(h), Space: O(h)
- delete(val): Delete from BST | Time: O(h), Space: O(h)

### 15_dynamic_programming.py
- fibonacci_dp(n): Fibonacci DP | Time: O(n), Space: O(n)
- climbing_stairs(n): Count ways to climb | Time: O(n), Space: O(n)
- coin_change(coins, amount): Min coins for amount | Time: O(amount*coins), Space: O(amount)
- longest_increasing_subsequence(arr): LIS length | Time: O(n²), Space: O(n)
- longest_common_subsequence(s1, s2): LCS length | Time: O(m*n), Space: O(m*n)
- knapsack_01(weights, values, capacity): 0/1 Knapsack | Time: O(n*capacity), Space: O(n*capacity)
- edit_distance(s1, s2): Min edits to convert | Time: O(m*n), Space: O(m*n)
- max_subarray_sum(arr): Kadane's algorithm | Time: O(n), Space: O(1)
- house_robber(arr): Max money without adjacent | Time: O(n), Space: O(n)

### And more in files 11-24...

## Quick Reference by Complexity

### O(1) Operations:
- Array access, Stack push/pop, Queue enqueue/dequeue, Hash insert/get

### O(log n) Operations:
- Binary search, Balanced BST operations, Heap operations

### O(n) Operations:
- Linear search, Array traversal, DP problems, Hashing problems

### O(n log n) Operations:
- Merge sort, Quick sort, Heap sort

### O(n²) Operations:
- Bubble/Selection/Insertion sort, Some DP problems

### O(2^n) Operations:
- Subsets generation, Fibonacci (naive)

### O(n!) Operations:
- Permutations generation
