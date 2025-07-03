import sys
from collections import deque

input = sys.stdin.readline

n, m, v = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n + 1):
    graph[i].sort()

visited_dfs = [False] * (n + 1)
path_dfs = []

def dfs(node):
    visited_dfs[node] = True
    path_dfs.append(node)
    for next_node in graph[node]:
        if not visited_dfs[next_node]:
            dfs(next_node)

visited_bfs = [False] * (n + 1)
path_bfs = []

def bfs(start_node):
    queue = deque([start_node])
    visited_bfs[start_node] = True

    while queue:
        node = queue.popleft()
        path_bfs.append(node)
        for next_node in graph[node]:
            if not visited_bfs[next_node]:
                queue.append(next_node)
                visited_bfs[next_node] = True

dfs(v)
bfs(v)

print(*path_dfs)
print(*path_bfs)