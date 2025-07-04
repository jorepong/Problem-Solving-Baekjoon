n = int(input())
map = [list(map(int, input())) for _ in range(n)]


def dfs(x, y):
    map[x][y] = 0
    ret = 1

    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and map[nx][ny] != 0:
            ret += dfs(nx, ny)

    return ret

result = []
for i in range(n):
    for j in range(n):
        if map[i][j] == 1:
            result.append(dfs(i, j))

print(len(result))
result.sort()
for c in result:
    print(c)
