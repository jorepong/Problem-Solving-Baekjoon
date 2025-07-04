import sys
from collections import deque

n, m = map(int, sys.stdin.readline().strip().split())

maze = []
visited = [[False]*m for _ in range(n)]
for _ in range(n):
    maze.append(list(map(int, sys.stdin.readline().strip())))

def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = True

    while queue:
        current_x, current_y = queue.popleft()

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            to_x, to_y = current_x + dx, current_y + dy
            if 0 <= to_x < n and 0 <= to_y < m and maze[to_x][to_y] != 0 and not visited[to_x][to_y]:
                if to_x == n-1 and to_y == m-1:
                    return maze[current_x][current_y] + 1

                visited[to_x][to_y] = True
                queue.append((to_x, to_y))
                maze[to_x][to_y] = maze[current_x][current_y] + 1

    return 0

print(bfs(0, 0))