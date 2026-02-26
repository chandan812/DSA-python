"""
GRAPH ALGORITHMS - Shortest Path, MST

THEORY:

1. DIJKSTRA'S ALGORITHM:
   - Single source shortest path
   - Works with non-negative weights
   - Uses priority queue (min heap)
   - Time: O((V+E) log V) with heap
   - Greedy approach

2. BELLMAN-FORD:
   - Single source shortest path
   - Handles negative weights
   - Detects negative cycles
   - Time: O(V*E)
   - Dynamic programming approach

3. FLOYD-WARSHALL:
   - All pairs shortest path
   - Time: O(V³)
   - Space: O(V²)
   - DP approach

4. KRUSKAL'S MST:
   - Minimum Spanning Tree
   - Sort edges, use Union-Find
   - Time: O(E log E)
   - Greedy approach

5. PRIM'S MST:
   - Minimum Spanning Tree
   - Grow tree from single vertex
   - Time: O(E log V) with heap
   - Greedy approach

WHEN TO USE:
- Dijkstra: Non-negative weights, single source
- Bellman-Ford: Negative weights, detect cycles
- Floyd-Warshall: All pairs, dense graph
- Kruskal: Sparse graph, edge-based
- Prim: Dense graph, vertex-based
"""
import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]
    while pq:
        curr_dist, curr_node = heapq.heappop(pq)
        if curr_dist > distances[curr_node]:
            continue
        for neighbor, weight in graph[curr_node]:
            distance = curr_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    return distances

def bellman_ford(vertices, edges, start):
    distances = {v: float('inf') for v in range(vertices)}
    distances[start] = 0
    for _ in range(vertices - 1):
        for u, v, weight in edges:
            if distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight
    for u, v, weight in edges:
        if distances[u] + weight < distances[v]:
            return None
    return distances

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[py] = px
            self.rank[px] += 1
        return True

def kruskal(n, edges):
    edges.sort(key=lambda x: x[2])
    uf = UnionFind(n)
    mst = []
    for u, v, weight in edges:
        if uf.union(u, v):
            mst.append((u, v, weight))
    return mst

if __name__ == "__main__":
    graph = {
        0: [(1, 4), (2, 1)],
        1: [(3, 1)],
        2: [(1, 2), (3, 5)],
        3: []
    }
    print(f"Dijkstra from 0: {dijkstra(graph, 0)}")
    
    edges = [(0, 1, 4), (0, 2, 1), (2, 1, 2), (1, 3, 1), (2, 3, 5)]
    print(f"Bellman-Ford: {bellman_ford(4, edges, 0)}")
    
    print(f"Kruskal MST: {kruskal(4, edges)}")
