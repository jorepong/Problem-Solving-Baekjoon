import sys

sys.setrecursionlimit(10**6)

n, r = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n + 1)] 
for _ in range(n - 1):
    v1, v2 = map(int, sys.stdin.readline().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

values = [-1] * (n + 1)
visited = [False] * (n + 1)

leaf_count = int(sys.stdin.readline())
for _ in range(leaf_count):
    v, value = map(int, sys.stdin.readline().split())
    values[v] = value

def dfs(node, depth):
    visited[node] = True
    
    is_leaf = True
    
    if depth % 2 == 0:
        ret = -1
    else:
        ret = 10**9 + 1

    for v in graph[node]:
        if not visited[v]:
            is_leaf = False 
            
            child_value = dfs(v, depth + 1)
            
            if depth % 2 == 0:
                ret = max(ret, child_value)
            else:
                ret = min(ret, child_value)

    if is_leaf:
        return values[node]

    values[node] = ret
    return ret

dfs(r, 0)

q_count = int(sys.stdin.readline())
for _ in range(q_count):
    node = int(sys.stdin.readline())
    print(values[node])