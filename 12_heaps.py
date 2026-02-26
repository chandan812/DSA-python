"""
HEAPS - Complete Binary Tree

THEORY:
- Complete binary tree with heap property
- Min Heap: Parent ≤ Children
- Max Heap: Parent ≥ Children
- Root contains min/max element
- Implemented using arrays for efficiency

ARRAY REPRESENTATION:
- Parent of i: (i-1)//2
- Left child of i: 2*i + 1
- Right child of i: 2*i + 2

OPERATIONS:
- Insert: Add at end, heapify up - O(log n)
- Delete/Extract: Remove root, heapify down - O(log n)
- Peek: View root - O(1)
- Build Heap: From array - O(n)

HEAPIFY:
- Up: Compare with parent, swap if needed
- Down: Compare with children, swap with smaller/larger

APPLICATIONS:
1. Priority Queue
2. Heap Sort - O(n log n)
3. K largest/smallest elements
4. Median in stream
5. Merge K sorted arrays
6. Dijkstra's shortest path

ADVANTAGES:
- Fast min/max access: O(1)
- Efficient insert/delete: O(log n)
- Space efficient (array-based)

COMMON PROBLEMS:
- Kth largest element
- Top K frequent elements
- Merge K sorted lists
- Find median from data stream
"""
import heapq

class MinHeap:
    def __init__(self):
        self.heap = []
    
    def push(self, val):
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)
    
    def pop(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root
    
    def peek(self):
        return self.heap[0] if self.heap else None
    
    def _heapify_up(self, idx):
        parent = (idx - 1) // 2
        if idx > 0 and self.heap[idx] < self.heap[parent]:
            self.heap[idx], self.heap[parent] = self.heap[parent], self.heap[idx]
            self._heapify_up(parent)
    
    def _heapify_down(self, idx):
        smallest = idx
        left = 2 * idx + 1
        right = 2 * idx + 2
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != idx:
            self.heap[idx], self.heap[smallest] = self.heap[smallest], self.heap[idx]
            self._heapify_down(smallest)

def kth_largest(arr, k):
    return heapq.nlargest(k, arr)[-1]

def kth_smallest(arr, k):
    return heapq.nsmallest(k, arr)[-1]

def top_k_frequent(arr, k):
    from collections import Counter
    count = Counter(arr)
    return heapq.nlargest(k, count.keys(), key=count.get)

if __name__ == "__main__":
    print("=== MIN HEAP ===")
    mh = MinHeap()
    for val in [5, 3, 7, 1, 9]:
        mh.push(val)
    print(f"Pop: {mh.pop()}")
    print(f"Peek: {mh.peek()}")
    
    print("\n=== KTH LARGEST/SMALLEST ===")
    arr = [3, 2, 1, 5, 6, 4]
    print(f"3rd Largest: {kth_largest(arr, 3)}")
    print(f"2nd Smallest: {kth_smallest(arr, 2)}")
    
    print("\n=== TOP K FREQUENT ===")
    print(top_k_frequent([1, 1, 1, 2, 2, 3], 2))
