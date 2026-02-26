"""
ADVANCED GRAPH ALGORITHMS

THEORY:

1. TARJAN'S SCC (Strongly Connected Components):
   - Find SCCs in directed graph
   - Uses DFS with low-link values
   - Time: O(V+E)
   - Single pass algorithm

2. KOSARAJU'S SCC:
   - Two-pass DFS algorithm
   - First: Find finish times
   - Second: DFS on transposed graph
   - Time: O(V+E)

3. ARTICULATION POINTS:
   - Vertices whose removal increases components
   - Critical nodes in network
   - Time: O(V+E)
   - Uses DFS with discovery/low times

4. BRIDGES:
   - Edges whose removal increases components
   - Critical connections
   - Time: O(V+E)

5. NETWORK FLOW:
   - Ford-Fulkerson: O(E * max_flow)
   - Edmonds-Karp: O(VE²)
   - Dinic's: O(V²E)

APPLICATIONS:
- SCC: Web graph analysis, recommendation systems
- Articulation Points: Network reliability
- Bridges: Critical infrastructure
- Network Flow: Max matching, min cut

CONCEPTS:
- SCC: Maximal set where every vertex reaches every other
- Cut Vertex: Removal disconnects graph
- Bridge: Removal increases components
"""
from collections import defaultdict, deque

def tarjan_scc(graph):
    index_counter = [0]
    stack = []
    lowlinks = {}
    index = {}
    on_stack = defaultdict(bool)
    sccs = []
    
    def strongconnect(node):
        index[node] = index_counter[0]
        lowlinks[node] = index_counter[0]
        index_counter[0] += 1
        stack.append(node)
        on_stack[node] = True
        
        for successor in graph[node]:
            if successor not in index:
                strongconnect(successor)
                lowlinks[node] = min(lowlinks[node], lowlinks[successor])
            elif on_stack[successor]:
                lowlinks[node] = min(lowlinks[node], index[successor])
        
        if lowlinks[node] == index[node]:
            scc = []
            while True:
                successor = stack.pop()
                on_stack[successor] = False
                scc.append(successor)
                if successor == node:
                    break
            sccs.append(scc)
    
    for node in graph:
        if node not in index:
            strongconnect(node)
    return sccs

def kosaraju_scc(graph):
    visited = set()
    stack = []
    
    def dfs1(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs1(neighbor)
        stack.append(node)
    
    for node in graph:
        if node not in visited:
            dfs1(node)
    
    transposed = defaultdict(list)
    for node in graph:
        for neighbor in graph[node]:
            transposed[neighbor].append(node)
    
    visited.clear()
    sccs = []
    
    def dfs2(node, scc):
        visited.add(node)
        scc.append(node)
        for neighbor in transposed[node]:
            if neighbor not in visited:
                dfs2(neighbor, scc)
    
    while stack:
        node = stack.pop()
        if node not in visited:
            scc = []
            dfs2(node, scc)
            sccs.append(scc)
    return sccs

def articulation_points(graph):
    visited = set()
    disc = {}
    low = {}
    parent = {}
    ap = set()
    time = [0]
    
    def dfs(u):
        children = 0
        visited.add(u)
        disc[u] = low[u] = time[0]
        time[0] += 1
        
        for v in graph[u]:
            if v not in visited:
                children += 1
                parent[v] = u
                dfs(v)
                low[u] = min(low[u], low[v])
                if parent.get(u) is None and children > 1:
                    ap.add(u)
                if parent.get(u) is not None and low[v] >= disc[u]:
                    ap.add(u)
            elif v != parent.get(u):
                low[u] = min(low[u], disc[v])
    
    for node in graph:
        if node not in visited:
            parent[node] = None
            dfs(node)
    return list(ap)

def bridges(graph):
    visited = set()
    disc = {}
    low = {}
    parent = {}
    bridges_list = []
    time = [0]
    
    def dfs(u):
        visited.add(u)
        disc[u] = low[u] = time[0]
        time[0] += 1
        
        for v in graph[u]:
            if v not in visited:
                parent[v] = u
                dfs(v)
                low[u] = min(low[u], low[v])
                if low[v] > disc[u]:
                    bridges_list.append((u, v))
            elif v != parent.get(u):
                low[u] = min(low[u], disc[v])
    
    for node in graph:
        if node not in visited:
            parent[node] = None
            dfs(node)
    return bridges_list

if __name__ == "__main__":
    graph = {0: [1], 1: [2], 2: [0, 3], 3: [4], 4: [5, 7], 5: [6], 6: [4], 7: []}
    print(f"Tarjan SCC: {tarjan_scc(graph)}")
    print(f"Kosaraju SCC: {kosaraju_scc(graph)}")
    
    graph2 = {0: [1, 2], 1: [0, 2], 2: [0, 1, 3], 3: [2, 4], 4: [3]}
    print(f"Articulation Points: {articulation_points(graph2)}")
    print(f"Bridges: {bridges(graph2)}")
