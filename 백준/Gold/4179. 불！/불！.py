import sys
from collections import deque


def solve():
    R, C = map(int, sys.stdin.readline().strip().split())
    maze = [list(map(str, sys.stdin.readline().strip())) for _ in range(R)]
    fire = [[float('inf')] * C for _ in range(R)]
    jihun = [[float('inf')] * C for _ in range(R)]

    queue_fire = deque()
    queue = deque()

    for i in range(R):
        for j in range(C):
            if maze[i][j] == 'F':
                fire[i][j] = 0
                queue_fire.append((i, j))
            elif maze[i][j] == 'J':
                jihun[i][j] = 0
                queue.append((i, j))

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while queue_fire:
        x, y = queue_fire.popleft()
        time = fire[x][y]

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < R and 0 <= ny < C and maze[nx][ny] != '#' and fire[nx][ny] == float('inf'):
                fire[nx][ny] = time + 1
                queue_fire.append((nx, ny))

    while queue:
        x, y = queue.popleft()
        time = jihun[x][y]

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if not (0 <= nx < R and 0 <= ny < C):
                print(time + 1)
                return

            if maze[nx][ny] == '#' or jihun[nx][ny] != float('inf'):
                continue

            if fire[nx][ny] == float('inf') or time + 1 < fire[nx][ny]:
                jihun[nx][ny] = time + 1
                queue.append((nx, ny))

    print('IMPOSSIBLE')


solve()