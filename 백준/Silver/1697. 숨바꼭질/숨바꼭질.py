import sys
from collections import deque

n, k = map(int, sys.stdin.readline().strip().split())

queue = deque([(n, 0)])
visited = [False] * 100001

while queue:
    item, day = queue.popleft()

    if item < 0 or item > 100000 or visited[item]:
        continue

    if item == k:
        print(day)
        break

    visited[item] = True

    queue.append((item+1, day+1))
    queue.append((item-1, day+1))
    queue.append((item*2, day+1))