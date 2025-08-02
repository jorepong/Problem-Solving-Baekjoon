import sys

n, m = map(int, sys.stdin.readline().split())
board = []
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))

def dfs(x, y, remain, visited):
    if remain == 1:
        return board[x][y]

    ret = -float('inf')
    for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in visited:
            visited.add((nx, ny))
            ret = max(ret, board[x][y] + dfs(nx, ny, remain - 1, visited))
            visited.remove((nx, ny))

    return ret

t_shapes = [
    [(0, 0), (0, 1), (0, 2), (1, 1)],
    [(0, 0), (0, 1), (0, 2), (-1, 1)],
    [(0, 0), (1, 0), (2, 0), (1, 1)],
    [(0, 0), (1, 0), (2, 0), (1, -1)],
]
def search_t_shape(x, y):
    ret = -float('inf')
    for t_shape in t_shapes:
        sum = 0
        for dx, dy in t_shape:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                sum += board[nx][ny]
            else:
                sum = 0
                break
        ret = max(ret, sum)
    return ret

ans = -float('inf')
for x in range(n):
    for y in range(m):
        ans = max(ans, dfs(x, y, 4, {(x, y)}))
        ans = max(ans, search_t_shape(x, y))

print(ans)