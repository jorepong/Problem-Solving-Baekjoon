import sys
sys.setrecursionlimit(10**6)

N, M = map(int, sys.stdin.readline().strip().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, sys.stdin.readline().strip().split())
    graph[u].append(v)
    graph[v].append(u)

connected_component = 0

nodes_in_graph = set()
for i in range(1, N+1):
    if graph[i]:
        nodes_in_graph.add(i)
        
connected_component += N - len(nodes_in_graph)

visited = set()

def dfs(key):
    if key in visited:
        return
    visited.add(key)
    for k in graph[key]:
        dfs(k)

for v in range(1, N+1):
    if graph[v] and v not in visited:
        dfs(v)
        connected_component += 1

print(connected_component)