"""
GRAPHS - Vertices and Edges
"""
from collections import deque, defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
    
    def bfs(self, start):
        visited = set()
        queue = deque([start])
        visited.add(start)
        result = []
        while queue:
            node = queue.popleft()
            result.append(node)
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return result
    
    def dfs(self, start):
        visited = set()
        result = []
        def dfs_helper(node):
            visited.add(node)
            result.append(node)
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    dfs_helper(neighbor)
        dfs_helper(start)
        return result
    
    def has_cycle(self):
        visited = set()
        rec_stack = set()
        def has_cycle_util(node):
            visited.add(node)
            rec_stack.add(node)
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    if has_cycle_util(neighbor):
                        return True
                elif neighbor in rec_stack:
                    return True
            rec_stack.remove(node)
            return False
        for node in self.graph:
            if node not in visited:
                if has_cycle_util(node):
                    return True
        return False
    
    def topological_sort(self):
        visited = set()
        stack = []
        def topo_util(node):
            visited.add(node)
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    topo_util(neighbor)
            stack.append(node)
        for node in self.graph:
            if node not in visited:
                topo_util(node)
        return stack[::-1]

if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    
    print(f"BFS from 0: {g.bfs(0)}")
    print(f"DFS from 0: {g.dfs(0)}")
    
    g2 = Graph()
    g2.add_edge(0, 1)
    g2.add_edge(1, 2)
    g2.add_edge(2, 0)
    print(f"Has cycle: {g2.has_cycle()}")
    
    g3 = Graph()
    g3.add_edge(5, 2)
    g3.add_edge(5, 0)
    g3.add_edge(4, 0)
    g3.add_edge(4, 1)
    g3.add_edge(2, 3)
    g3.add_edge(3, 1)
    print(f"Topological Sort: {g3.topological_sort()}")
