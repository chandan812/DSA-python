"""
QUEUES - FIFO (First In First Out)

THEORY:
- Linear data structure following FIFO principle
- Elements added at rear, removed from front
- Like a line of people - first come, first served
- Can be implemented using arrays or linked lists

OPERATIONS:
- Enqueue: Add element at rear - O(1)
- Dequeue: Remove element from front - O(1)
- Front/Peek: View front element - O(1)
- isEmpty: Check if empty - O(1)

TYPES:
1. Simple Queue - Basic FIFO
2. Circular Queue - Last position connects to first
3. Priority Queue - Elements have priority
4. Deque (Double-ended) - Insert/delete from both ends

SPACE COMPLEXITY: O(n)

APPLICATIONS:
1. CPU scheduling
2. Disk scheduling
3. BFS traversal
4. Print queue
5. Call center systems
6. Handling requests in web servers

COMMON PROBLEMS:
- First non-repeating character in stream
- Generate binary numbers
- Sliding window maximum
- Level order traversal

WHEN TO USE:
- Need FIFO access pattern
- Order preservation important
- BFS algorithms
- Resource sharing (CPU, printer)
"""
from collections import deque

class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        return self.items.pop(0) if not self.is_empty() else None
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)

class CircularQueue:
    def __init__(self, k):
        self.queue = [None] * k
        self.size = k
        self.front = self.rear = -1
    
    def enqueue(self, value):
        if (self.rear + 1) % self.size == self.front:
            return False
        if self.front == -1:
            self.front = 0
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = value
        return True
    
    def dequeue(self):
        if self.front == -1:
            return None
        val = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return val

def reverse_queue(q):
    stack = []
    while not q.is_empty():
        stack.append(q.dequeue())
    while stack:
        q.enqueue(stack.pop())
    return q

def first_non_repeating_stream(stream):
    from collections import Counter
    count = Counter()
    queue = deque()
    result = []
    for char in stream:
        count[char] += 1
        queue.append(char)
        while queue and count[queue[0]] > 1:
            queue.popleft()
        result.append(queue[0] if queue else '#')
    return result

if __name__ == "__main__":
    print("=== QUEUE ===")
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(f"Dequeue: {q.dequeue()}")
    
    print("\n=== CIRCULAR QUEUE ===")
    cq = CircularQueue(3)
    cq.enqueue(1)
    cq.enqueue(2)
    print(f"Dequeue: {cq.dequeue()}")
    
    print("\n=== FIRST NON-REPEATING ===")
    print(first_non_repeating_stream("aabccxb"))
