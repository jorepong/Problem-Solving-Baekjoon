from collections import defaultdict, deque

n, m = map(int, input().split())
graph = defaultdict(list)

for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)

visited = [False] * (n+1)
result = []

def dfs(node):
    visited[node] = True

    for next_node in graph[node]:
        if not visited[next_node]:
            dfs(next_node)

    result.append(node)

for node in range(1, n+1):
    if not visited[node]:
        dfs(node)

print(*result[::-1])