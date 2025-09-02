import sys
sys.setrecursionlimit(10**8)

def solution(maps):
    answer = []
    h = len(maps)
    w = len(maps[0])
    
    visited = [[False] * w for _ in range(h)]
    
    def dfs(x, y):
        visited[x][y] = True
        food = int(maps[x][y])
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < h and 0 <= ny < w and maps[nx][ny] != 'X' and not visited[nx][ny]:
                food += dfs(nx, ny)
        
        return food
    
    for i in range(h):
        for j in range(w):
            if maps[i][j] != 'X' and not visited[i][j]:
                answer.append(dfs(i, j))
    
    return sorted(answer) if len(answer) > 0 else [-1]