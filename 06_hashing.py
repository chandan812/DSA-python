"""
HASHING - Key-Value Storage

THEORY:
- Maps keys to values using hash function
- Hash function converts key to array index
- Provides O(1) average case for insert, search, delete
- Collision handling: Chaining or Open Addressing

HASH FUNCTION:
- Converts key to integer (hash code)
- Maps hash code to array index: index = hash(key) % table_size
- Good hash function: uniform distribution, deterministic

COLLISION RESOLUTION:
1. Chaining - Store multiple elements at same index (linked list)
2. Open Addressing - Find next available slot (linear/quadratic probing)

TIME COMPLEXITY:
- Average: O(1) for insert, search, delete
- Worst: O(n) when all keys collide

SPACE COMPLEXITY: O(n)

APPLICATIONS:
- Database indexing
- Caching (LRU cache)
- Symbol tables in compilers
- Password verification
- Counting frequencies

COMMON PROBLEMS:
- Two Sum
- Subarray with given sum
- Longest consecutive sequence
- Group anagrams
"""

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]
    
    def hash_function(self, key):
        return hash(key) % self.size
    
    def insert(self, key, value):
        index = self.hash_function(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        self.table[index].append((key, value))
    
    def get(self, key):
        index = self.hash_function(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None
    
    def delete(self, key):
        index = self.hash_function(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return True
        return False

def two_sum(arr, target):
    seen = {}
    for i, num in enumerate(arr):
        if target - num in seen:
            return [seen[target - num], i]
        seen[num] = i
    return []

def subarray_sum_zero(arr):
    sum_map = {0: -1}
    curr_sum = 0
    for i, num in enumerate(arr):
        curr_sum += num
        if curr_sum in sum_map:
            return True
        sum_map[curr_sum] = i
    return False

def longest_subarray_sum_k(arr, k):
    sum_map = {}
    curr_sum = max_len = 0
    for i, num in enumerate(arr):
        curr_sum += num
        if curr_sum == k:
            max_len = i + 1
        if curr_sum - k in sum_map:
            max_len = max(max_len, i - sum_map[curr_sum - k])
        if curr_sum not in sum_map:
            sum_map[curr_sum] = i
    return max_len

def count_distinct_elements(arr):
    return len(set(arr))

def find_duplicates(arr):
    seen = set()
    duplicates = set()
    for num in arr:
        if num in seen:
            duplicates.add(num)
        seen.add(num)
    return list(duplicates)

if __name__ == "__main__":
    print("=== HASH TABLE ===")
    ht = HashTable()
    ht.insert("name", "Alice")
    ht.insert("age", 25)
    print(f"Get name: {ht.get('name')}")
    
    print("\n=== TWO SUM ===")
    print(two_sum([2, 7, 11, 15], 9))
    
    print("\n=== SUBARRAY SUM ZERO ===")
    print(subarray_sum_zero([4, 2, -3, 1, 6]))
    
    print("\n=== LONGEST SUBARRAY SUM K ===")
    print(longest_subarray_sum_k([10, 5, 2, 7, 1, 9], 15))
    
    print("\n=== COUNT DISTINCT ===")
    print(count_distinct_elements([1, 2, 2, 3, 4, 4, 5]))
    
    print("\n=== FIND DUPLICATES ===")
    print(find_duplicates([1, 2, 3, 2, 4, 3, 5]))
