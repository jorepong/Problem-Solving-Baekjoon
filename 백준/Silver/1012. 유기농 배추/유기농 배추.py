import sys

sys.setrecursionlimit(10**6)
t = int(sys.stdin.readline().strip())

def dfs(field, x, y):
    field[x][y] = 0

    for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        if 0 <= x+i < len(field) and 0 <= y+j < len(field[0]):
            if field[x+i][y+j] == 1:
                dfs(field, x+i, y+j)


for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().strip().split())
    field = [[0 for _ in range(n)] for _ in range(m)]

    for _ in range(k):
        x, y = map(int, sys.stdin.readline().strip().split())
        field[x][y] = 1

    count = 0
    for x in range(m):
        for y in range(n):
            if field[x][y] == 1:
                count += 1
                dfs(field, x, y)

    print(count)