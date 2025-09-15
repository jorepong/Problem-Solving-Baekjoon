import heapq
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1)

for _ in range(M):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    indegree[n2] += 1

heap = []
for i in range(1, N+1):
    if indegree[i] == 0:
        heapq.heappush(heap, i)

result = []
queue = deque([heapq.heappop(heap)])
while queue:
    item = queue.popleft()
    result.append(item)

    for child in graph[item]:
        indegree[child] -= 1
        if indegree[child] == 0:
            heapq.heappush(heap, child)

    if heap:
        queue.append(heapq.heappop(heap))

print(*result)