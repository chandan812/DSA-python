"""
LINKED LISTS - Dynamic Linear Data Structure
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
    
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
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
    
    def display(self):
        elements = []
        curr = self.head
        while curr:
            elements.append(str(curr.data))
            curr = curr.next
        return " -> ".join(elements)
    
    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev
    
    def detect_cycle(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
    
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
