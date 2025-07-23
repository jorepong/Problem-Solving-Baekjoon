import sys

sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline().strip())
graph = []

for _ in range(n):
    graph.append(list(map(str, sys.stdin.readline().strip())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def dfs(x, y, disabled = False):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
            if (graph[nx][ny] == graph[x][y] or
                (disabled and (graph[x][y] == 'R' or graph[x][y] == 'G') and (graph[nx][ny] == 'R' or graph[nx][ny] == 'G'))):
                visited[nx][ny] = True
                dfs(nx, ny, disabled)

count = [0, 0]
for i, disabled in enumerate([False, True]):
    visited = [[False] * n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if not visited[x][y]:
                dfs(x, y, disabled)
                count[i] += 1

print(*count)