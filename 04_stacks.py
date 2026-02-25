"""
STACKS - LIFO (Last In First Out)
"""

class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop() if not self.is_empty() else None
    
    def peek(self):
        return self.items[-1] if not self.is_empty() else None
    
    def is_empty(self):
        return len(self.items) == 0

def is_balanced(expression):
    stack = []
    pairs = {'(': ')', '{': '}', '[': ']'}
    for char in expression:
        if char in pairs:
            stack.append(char)
        elif char in pairs.values():
            if not stack or pairs[stack.pop()] != char:
                return False
    return len(stack) == 0

def next_greater_element(arr):
    result = [-1] * len(arr)
    stack = []
    for i in range(len(arr) - 1, -1, -1):
        while stack and stack[-1] <= arr[i]:
            stack.pop()
        if stack:
            result[i] = stack[-1]
        stack.append(arr[i])
    return result

def evaluate_postfix(expression):
    stack = []
    for char in expression.split():
        if char.isdigit():
            stack.append(int(char))
        else:
            b = stack.pop()
            a = stack.pop()
            if char == '+':
                stack.append(a + b)
            elif char == '-':
                stack.append(a - b)
            elif char == '*':
                stack.append(a * b)
            elif char == '/':
                stack.append(a // b)
    return stack[0]

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
    
    def push(self, val):
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
    
    def pop(self):
        if self.stack:
            val = self.stack.pop()
            if val == self.min_stack[-1]:
                self.min_stack.pop()
            return val
    
    def get_min(self):
        return self.min_stack[-1] if self.min_stack else None

if __name__ == "__main__":
    print("=== STACK ===")
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(f"Pop: {s.pop()}")
    print(f"Peek: {s.peek()}")
    
    print("\n=== BALANCED PARENTHESES ===")
    print(is_balanced("({[]})"))
    
    print("\n=== NEXT GREATER ELEMENT ===")
    print(next_greater_element([4, 5, 2, 10, 8]))
    
    print("\n=== POSTFIX EVALUATION ===")
    print(evaluate_postfix("2 3 1 * + 9 -"))
    
    print("\n=== MIN STACK ===")
    ms = MinStack()
    ms.push(3)
    ms.push(5)
    ms.push(2)
    print(f"Min: {ms.get_min()}")
