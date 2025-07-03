from collections import defaultdict, deque


def dfs(graph, start, visited):
    if start in visited:
        return

    visited.append(start)

    for v in graph[start]:
        dfs(graph, v, visited)

def bfs(graph, start, visited):
    queue = deque([start])

    while queue:
        v = queue.popleft()

        if v in visited:
            continue

        visited.append(v)

        for s in graph[v]:
            if s not in visited:
                queue.append(s)


def solve():
    N, M, V = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(M):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)

    for i in range(1, N+1):
        graph[i].sort()

    path = []
    dfs(graph, V, path)

    path2 = []
    bfs(graph, V, path2)

    print(' '.join(list(map(str, path))))
    print(' '.join(list(map(str, path2))))


if __name__ == "__main__":
    solve()