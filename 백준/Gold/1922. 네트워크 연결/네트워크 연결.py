import heapq
import sys
from collections import defaultdict

v = int(sys.stdin.readline())
e = int(sys.stdin.readline())
graph = defaultdict(list)

for _ in range(e):
    a, b, weight = map(int, sys.stdin.readline().split())
    graph[a].append((b, weight))
    graph[b].append((a, weight))

def prim(start):
    result = 0

    heap = []
    for node, weight in graph[start]:
        heapq.heappush(heap, (weight, node))

    visited = {start}
    count = 0
    while count < v-1:
        weight, target = heapq.heappop(heap)

        if target not in visited:
            result += weight
            visited.add(target)
            count += 1

            for node, w in graph[target]:
                heapq.heappush(heap, (w, node))

    return result


print(prim(1))