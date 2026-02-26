"""
GRAPHS - Vertices and Edges

THEORY:
- Non-linear data structure: G = (V, E)
- V = Set of vertices (nodes)
- E = Set of edges (connections)
- Can be directed or undirected, weighted or unweighted

REPRESENTATIONS:
1. Adjacency Matrix - 2D array, O(V²) space
   - Fast edge lookup: O(1)
   - Slow to iterate neighbors: O(V)
2. Adjacency List - Array of lists, O(V+E) space
   - Slow edge lookup: O(V)
   - Fast to iterate neighbors: O(degree)

TRAVERSALS:
1. BFS (Breadth-First Search):
   - Uses Queue
   - Level by level
   - Shortest path in unweighted graph
   - Time: O(V+E)

2. DFS (Depth-First Search):
   - Uses Stack/Recursion
   - Go deep first
   - Detect cycles, topological sort
   - Time: O(V+E)

COMMON PROBLEMS:
- Cycle Detection
- Topological Sort (DAG)
- Connected Components
- Bipartite Check
- Shortest Path
- Minimum Spanning Tree

APPLICATIONS:
- Social networks
- Maps and navigation
- Web crawling
- Network routing
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
