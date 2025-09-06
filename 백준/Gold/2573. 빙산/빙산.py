import sys
sys.setrecursionlimit(10**6)

n, m = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]


def dfs(x, y, visited):
    visited[x][y] = True

    for nx, ny in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        dx, dy = nx + x, ny + y
        if 0 <= dx < n and 0 <= dy < m and board[dx][dy] > 0 and not visited[dx][dy]:
            dfs(dx, dy, visited)

def solve():
    time = 0
    while True:
        count = 0
        visited = [[False] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if board[i][j] > 0 and not visited[i][j]:
                    dfs(i, j, visited)
                    count += 1

        if count == 0:
            return 0
        elif count == 1:
            sub_board = [[0] * m for _ in range(n)]
            for i in range(n):
                for j in range(m):
                    if board[i][j] > 0:
                        for nx, ny in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                            dx, dy = nx + i, ny + j
                            if 0 <= dx < n and 0 <= dy < m and board[dx][dy] <= 0:
                                sub_board[i][j] = sub_board[i][j] + 1

            for i in range(n):
                for j in range(m):
                    board[i][j] -= sub_board[i][j]
            time += 1
        else:
            return time

print(solve())