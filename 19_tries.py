"""
TRIE - Prefix Tree for efficient string operations
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
    
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end
    
    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
    
    def delete(self, word):
        def delete_helper(node, word, index):
            if index == len(word):
                if not node.is_end:
                    return False
                node.is_end = False
                return len(node.children) == 0
            char = word[index]
            if char not in node.children:
                return False
            should_delete = delete_helper(node.children[char], word, index + 1)
            if should_delete:
                del node.children[char]
                return len(node.children) == 0 and not node.is_end
            return False
        delete_helper(self.root, word, 0)

def autocomplete(trie, prefix):
    node = trie.root
    for char in prefix:
        if char not in node.children:
            return []
        node = node.children[char]
    
    results = []
    def dfs(node, path):
        if node.is_end:
            results.append(prefix + path)
        for char, child in node.children.items():
            dfs(child, path + char)
    dfs(node, "")
    return results

if __name__ == "__main__":
    trie = Trie()
    words = ["apple", "app", "apricot", "banana"]
    for word in words:
        trie.insert(word)
    
    print(f"Search 'app': {trie.search('app')}")
    print(f"Starts with 'ap': {trie.starts_with('ap')}")
    print(f"Autocomplete 'ap': {autocomplete(trie, 'ap')}")
