import sys
sys.setrecursionlimit(10**6)

m, n = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
dp = [[-1] * n for _ in range(m)]
dp[m-1][n-1] = 1

def get_route_num(i, j):
    if dp[i][j] != -1:
        return dp[i][j]

    dp[i][j] = 0
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = dx + i, dy + j
        if 0 <= nx < m and 0 <= ny < n:
            if board[nx][ny] < board[i][j]:
                dp[i][j] += get_route_num(nx, ny)

    return dp[i][j]

print(get_route_num(0, 0))