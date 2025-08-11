import sys
from collections import defaultdict, deque

t = int(sys.stdin.readline())

def solve(graph, v):
    check = [0] * v

    for i in range(v):
        if check[i] != 0:
            continue
        check[i] = 1
        queue = deque([(i, 1)])  # (node, marker)
        while queue:
            node, marker = queue.popleft()

            for target in graph[node]:
                if check[target] == marker:
                    return False
                elif check[target] == 0:
                    check[target] = 3 - marker
                    queue.append((target, 3 - marker))
    return True


for _ in range(t):
    v, e = map(int, sys.stdin.readline().split())
    graph = defaultdict(list)

    for _ in range(e):
        v1, v2 = map(int, sys.stdin.readline().split())
        graph[v1-1].append(v2-1)
        graph[v2-1].append(v1-1)

    print('YES' if solve(graph, v) else 'NO')
