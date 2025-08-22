import sys
from collections import deque

n, l, r = map(int, sys.stdin.readline().split())
land = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

def check():
    for i in range(n):
        for j in range(n):
            if i + 1 < n:
                if l <= abs(land[i][j] - land[i+1][j]) <= r:
                    return True
            if j + 1 < n:
                if l <= abs(land[i][j] - land[i][j+1]) <= r:
                    return True

    return False

count = 0
while check():
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                continue

            sum_of_region = 0
            region = set()
            queue = deque([(i, j)])
            while queue:
                x, y = queue.popleft()
                if visited[x][y]:
                    continue
                visited[x][y] = True
                sum_of_region += land[x][y]
                region.add((x, y))

                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x + dx, y + dy
                    if (0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and
                            l <= abs(land[x][y] - land[nx][ny]) <= r):
                        queue.append((nx, ny))

            for country in region:
                x, y = country
                land[x][y] = sum_of_region // len(region)
    count += 1

print(count)