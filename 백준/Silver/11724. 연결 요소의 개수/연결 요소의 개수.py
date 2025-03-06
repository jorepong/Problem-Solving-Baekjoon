import sys

sys.setrecursionlimit(10 ** 6)

N, M = map(int, sys.stdin.readline().strip().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, sys.stdin.readline().strip().split())
    graph[u].append(v)
    graph[v].append(u)

connected_component = 0
visited = [False] * (N + 1)

def dfs(index):
    visited[index] = True
    for k in graph[index]:
        if not visited[k]:
            dfs(k)

for i in range(1, N + 1):
    if not visited[i]:
        dfs(i)
        connected_component += 1

print(connected_component)