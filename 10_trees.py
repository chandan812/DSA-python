"""
TREES - Hierarchical Data Structure

THEORY:
- Non-linear hierarchical structure
- Root node at top, children below
- Each node has at most one parent
- Nodes without children are leaves

TERMINOLOGY:
- Root: Top node (no parent)
- Parent: Node with children
- Child: Node with parent
- Leaf: Node without children
- Height: Longest path from node to leaf
- Depth: Distance from root to node
- Level: Depth + 1

BINARY TREE:
- Each node has at most 2 children (left, right)
- Types: Full, Complete, Perfect, Balanced

BINARY SEARCH TREE (BST):
- Left subtree < Node < Right subtree
- Enables O(log n) search in balanced tree
- Degrades to O(n) if unbalanced

TRAVERSALS:
1. Inorder (Left-Root-Right) - Gives sorted order in BST
2. Preorder (Root-Left-Right) - Copy tree
3. Postorder (Left-Right-Root) - Delete tree
4. Level Order (BFS) - Level by level

TIME COMPLEXITY (Balanced BST):
- Search: O(log n)
- Insert: O(log n)
- Delete: O(log n)

APPLICATIONS:
- File systems
- Expression parsing
- Database indexing
- Huffman coding
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def inorder(self, node):
        return self.inorder(node.left) + [node.val] + self.inorder(node.right) if node else []
    
    def preorder(self, node):
        return [node.val] + self.preorder(node.left) + self.preorder(node.right) if node else []
    
    def postorder(self, node):
        return self.postorder(node.left) + self.postorder(node.right) + [node.val] if node else []
    
    def level_order(self, root):
        if not root:
            return []
        result, queue = [], [root]
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
        return result
    
    def height(self, node):
        return 0 if not node else 1 + max(self.height(node.left), self.height(node.right))

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, val):
        self.root = self._insert(self.root, val)
    
    def _insert(self, node, val):
        if not node:
            return TreeNode(val)
        if val < node.val:
            node.left = self._insert(node.left, val)
        else:
            node.right = self._insert(node.right, val)
        return node
    
    def search(self, val):
        return self._search(self.root, val)
    
    def _search(self, node, val):
        if not node or node.val == val:
            return node
        return self._search(node.left, val) if val < node.val else self._search(node.right, val)
    
    def inorder(self, node):
        return self.inorder(node.left) + [node.val] + self.inorder(node.right) if node else []

if __name__ == "__main__":
    bt = BinaryTree()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    
    print(f"Inorder: {bt.inorder(root)}")
    print(f"Preorder: {bt.preorder(root)}")
    print(f"Postorder: {bt.postorder(root)}")
    print(f"Level Order: {bt.level_order(root)}")
    print(f"Height: {bt.height(root)}")
    
    print("\n=== BST ===")
    bst = BST()
    for val in [50, 30, 70, 20, 40, 60, 80]:
        bst.insert(val)
    print(f"Inorder: {bst.inorder(bst.root)}")
    print(f"Search 40: {bst.search(40) is not None}")
