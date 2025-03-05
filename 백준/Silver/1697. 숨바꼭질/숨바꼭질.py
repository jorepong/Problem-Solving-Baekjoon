import sys
from collections import deque

n, k = map(int, sys.stdin.readline().strip().split())

queue = deque()
visited = set()

queue.append((n, 0))

while queue:
    item, day = queue.popleft()

    if item in visited or item < 0 or item > 100000:
        continue

    if item == k:
        print(day)
        break

    visited.add(item)

    queue.append((item+1, day+1))
    queue.append((item-1, day+1))
    queue.append((item*2, day+1))