import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)

n, r = map(int, sys.stdin.readline().strip().split())
graph = defaultdict(list)

for _ in range(n-1):
    v1, v2 = map(int, sys.stdin.readline().strip().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

values = [-1] * (n+1)
visited = [False] * (n+1)
for _ in range(int(sys.stdin.readline().strip())):
    v, value = map(int, sys.stdin.readline().strip().split())
    values[v] = value

def dfs(node, depth):
    if depth % 2 == 0:
        ret = -float('inf')
    else:
        ret = float('inf')

    visited[node] = True
    for v in graph[node]:
        if visited[v]:
            continue
        if depth % 2 == 0:
            ret = max(ret, dfs(v, depth + 1))
        else:
            ret = min(ret, dfs(v, depth + 1))

    if ret == float('inf') or ret == -float('inf'):
        return values[node]

    values[node] = ret
    return ret

dfs(r, 0)

q = int(sys.stdin.readline().strip())
for _ in range(q):
    node = int(input())
    print(values[node])