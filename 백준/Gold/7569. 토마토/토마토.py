from collections import deque

m, n, h = map(int, input().split())

boxes = []
visited = [[[-1] * m for _ in range(n)] for _ in range(h)]
for _ in range(h):
    box = []
    for _ in range(n):
        box.append(list(map(int, input().split())))
    boxes.append(box)


def bfs():
    queue = deque()
    for i, box in enumerate(boxes):
        for j, row in enumerate(box):
            for k, item in enumerate(row):
                if item == 1:
                    queue.append((i, j, k))
                    visited[i][j][k] = 0

    maximum = 0
    while queue:
        x, y, z = queue.popleft()

        for dx, dy, dz in [(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]:
            nx, ny, nz = x + dx, y + dy, z + dz

            if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m and visited[nx][ny][nz] == -1 and boxes[nx][ny][nz] == 0:
                queue.append((nx, ny, nz))
                boxes[nx][ny][nz] = -1
                visited[nx][ny][nz] = visited[x][y][z] + 1
                maximum = max(maximum, visited[nx][ny][nz])

    for i, box in enumerate(boxes):
        for j, row in enumerate(box):
            for k, item in enumerate(row):
                if item == 0:
                    return -1

    return maximum

print(bfs())
