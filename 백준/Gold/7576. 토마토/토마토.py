import sys
from collections import deque

m, n = map(int, sys.stdin.readline().strip().split())

arr = []

for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().strip().split())))

queue = deque()

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            queue.append((i, j, 0))

day_count = 0
while queue:
    tomato = queue.popleft()
    y = tomato[0]
    x = tomato[1]
    day = tomato[2]
    day_count = max(day, day_count)

    for (dy, dx) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        ny = y + dy
        nx = x + dx
        if 0 <= ny < n and 0 <= nx < m:
            if arr[ny][nx] == 0:
                arr[ny][nx] = 1
                queue.append((ny, nx, day+1))

possible = True
for row in arr:
    if 0 in row:
        possible = False
        break

if possible:
    print(day_count)
else:
    print(-1)