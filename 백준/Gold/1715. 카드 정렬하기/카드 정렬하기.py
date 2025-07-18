import heapq
from collections import deque

n = int(input())

heap = []
for _ in range(n):
    heapq.heappush(heap, int(input()))

comparing = 0
while len(heap) > 1:
    item1 = heapq.heappop(heap)
    item2 = heapq.heappop(heap)

    n = item1 + item2
    comparing += n
    heapq.heappush(heap, n)

print(comparing)