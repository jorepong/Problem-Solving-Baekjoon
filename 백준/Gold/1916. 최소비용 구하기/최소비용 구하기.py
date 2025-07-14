from collections import defaultdict

n = int(input())
m = int(input())
graph = defaultdict(list)
dist = [float('inf')] * (n+1)
visited = [False] * (n+1)

for _ in range(m):
    f, t, w = map(int, input().split())
    graph[f].append((t, w))

def get_smallest_node():
    smallest_weight = float('inf')
    node = 0
    for i in range(1, n+1):
        if dist[i] < smallest_weight and not visited[i]:
            smallest_weight = dist[i]
            node = i
    return node

def solve(start):
    visited[start] = True
    dist[start] = 0
    for node, weight in graph[start]:
        dist[node] = min(dist[node], weight)

    for _ in range(n-1):
        smallest_node = get_smallest_node()

        for node, weight in graph[smallest_node]:
            if visited[node]:
                continue
            if dist[node] == float('inf'):
                dist[node] = dist[smallest_node] + weight
            else:
                dist[node] = min(dist[node], dist[smallest_node] + weight)
        visited[smallest_node] = True

start, end = map(int, input().split())
solve(start)
print(dist[end])