import sys
from collections import defaultdict

n, e = map(int, sys.stdin.readline().strip().split())
graph = defaultdict(list)

for _ in range(e):
    v1, v2, w = map(int, sys.stdin.readline().strip().split())
    graph[v1].append((v2, w))
    graph[v2].append((v1, w))

v1, v2 = map(int, sys.stdin.readline().strip().split())

def dijkstra(start):
    dist = [float('inf')] * (n+1)
    dist[start] = 0
    visited = {start}

    for v, w in graph[start]:
        dist[v] = w

    for _ in range(n-1):
        node = 0
        min_distance = float('inf')
        for i in range(1, n+1):
            if i in visited or dist[i] == float('inf'):
                continue
            if dist[i] < min_distance:
                min_distance = dist[i]
                node = i

        for v, w in graph[node]:
            dist[v] = min(dist[v], dist[node] + w)
        visited.add(node)

    return dist

dist1 = dijkstra(1)
dist2 = dijkstra(n)
dist3 = dijkstra(v1)
v1_to_v2 = dist3[v2]

min_dist = min(dist1[v1] + v1_to_v2 + dist2[v2],
               dist1[v2] + v1_to_v2 + dist2[v1],
               dist1[v1] + v1_to_v2*2 + dist2[v1],
               dist1[v2] + v1_to_v2*2 + dist2[v2])

print(min_dist if min_dist < float('inf') else -1)