import heapq
import sys

n, k = map(int, sys.stdin.readline().split())

jewels = []
for _ in range(n):
    w, v = map(int, sys.stdin.readline().split())
    jewels.append((w, v))
jewels.sort()

bags = []
for _ in range(k):
    c = int(sys.stdin.readline())
    bags.append(c)
bags.sort()

total_value = 0
j = 0
heap = []
for bag in bags:
    while j < n and jewels[j][0] <= bag:
        heapq.heappush(heap, -jewels[j][1])
        j += 1
    if heap:
        total_value -= heapq.heappop(heap)

print(total_value)