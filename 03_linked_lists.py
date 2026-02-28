"""
LINKED LISTS - Dynamic Linear Data Structure

THEORY:
- Nodes connected via pointers/references
- Each node contains data and pointer to next node
- Dynamic size - grows/shrinks at runtime
- Non-contiguous memory allocation

TYPES:
1. Singly Linked List - One pointer (next)
2. Doubly Linked List - Two pointers (prev, next)
3. Circular Linked List - Last node points to first

TIME COMPLEXITY:
- Access: O(n) - Must traverse from head
- Search: O(n) - Linear traversal
- Insert at head: O(1)
- Insert at tail: O(n) without tail pointer, O(1) with tail
- Delete: O(n) - Need to find node first

SPACE COMPLEXITY: O(n) - Extra space for pointers

ADVANTAGES:
- Dynamic size
- Efficient insertion/deletion at beginning
- No memory waste

DISADVANTAGES:
- No random access
- Extra memory for pointers
- Not cache-friendly

COMMON TECHNIQUES:
1. Two Pointers (Fast & Slow) - Cycle detection, middle element
2. Dummy Node - Simplifies edge cases
3. Recursion - Reversal, traversal
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    # Insert at end of linked list
    # Time: O(n), Space: O(1)
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
    
    # Insert at beginning of linked list
    # Time: O(1), Space: O(1)
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    # Delete node with given key
    # Time: O(n), Space: O(1)
    def delete_node(self, key):
        curr = self.head
        if curr and curr.data == key:
            self.head = curr.next
            return
        prev = None
        while curr and curr.data != key:
            prev = curr
            curr = curr.next
        if curr:
            prev.next = curr.next
    
    # Display linked list as string
    # Time: O(n), Space: O(n)
    def display(self):
        elements = []
        curr = self.head
        while curr:
            elements.append(str(curr.data))
            curr = curr.next
        return " -> ".join(elements)
    
    # Reverse linked list in-place
    # Time: O(n), Space: O(1)
    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev
    
    # Detect cycle using Floyd's algorithm (fast & slow pointers)
    # Time: O(n), Space: O(1)
    def detect_cycle(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
    
    # Find middle element using fast & slow pointers
    # Time: O(n), Space: O(1)
    def find_middle(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data if slow else None

class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    # Insert at end of doubly linked list
    # Time: O(n), Space: O(1)
    def insert_at_end(self, data):
        new_node = DNode(data)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
        new_node.prev = curr
    
    # Display doubly linked list
    # Time: O(n), Space: O(n)
    def display(self):
        elements = []
        curr = self.head
        while curr:
            elements.append(str(curr.data))
            curr = curr.next
        return " <-> ".join(elements)

if __name__ == "__main__":
    print("=== SINGLY LINKED LIST ===")
    ll = LinkedList()
    for i in [1, 2, 3, 4, 5]:
        ll.insert_at_end(i)
    print(f"Original: {ll.display()}")
    
    ll.insert_at_beginning(0)
    print(f"After insert at beginning: {ll.display()}")
    
    ll.delete_node(3)
    print(f"After delete 3: {ll.display()}")
    
    print(f"Middle element: {ll.find_middle()}")
    
    ll.reverse()
    print(f"Reversed: {ll.display()}")
    
    print("\n=== DOUBLY LINKED LIST ===")
    dll = DoublyLinkedList()
    for i in [1, 2, 3, 4]:
        dll.insert_at_end(i)
    print(f"Doubly LL: {dll.display()}")
