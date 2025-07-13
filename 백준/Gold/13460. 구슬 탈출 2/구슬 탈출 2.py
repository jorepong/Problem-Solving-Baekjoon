from collections import deque

n, m = map(int, input().split())
board = []
visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
bx_init, by_init, rx_init, ry_init = 0, 0, 0, 0

for r in range(n):
    line = list(input())
    board.append(line)
    if line.__contains__('R'):
        c = line.index('R')
        rx_init = r
        ry_init = c
    if line.__contains__('B'):
        c = line.index('B')
        bx_init = r
        by_init = c

def move(x, y, dx, dy):
    count = 0
    if not (0 <= x+dx < n and y+dy < m):
        return x, y, count
    while board[x+dx][y+dy] != '#':
        x += dx
        y += dy
        count += 1
        if board[x][y] == 'O':
            break
    return x, y, count

def bfs(bx_init, by_init, rx_init, ry_init):
    queue = deque([(bx_init, by_init, rx_init, ry_init, 0)])
    visited[bx_init][by_init][rx_init][ry_init] = True

    while queue:
        bx, by, rx, ry, count = queue.popleft()
        if board[rx][ry] == 'O':
            if board[bx][by] == 'O':
                continue
            return count
        elif board[bx][by] == 'O':
            continue

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            rbx, rby, bc = move(bx, by, dx, dy)
            rrx, rry, rc = move(rx, ry, dx, dy)

            if rbx == rrx and rby == rry and board[rbx][rby] != 'O':
                if bc > rc:
                    rbx -= dx
                    rby -= dy
                else:
                    rrx -= dx
                    rry -= dy
            if not visited[rbx][rby][rrx][rry]:
                visited[rbx][rby][rrx][rry] = True
                queue.append((rbx, rby, rrx, rry, count+1))

    return -1

result = bfs(bx_init, by_init, rx_init, ry_init)
print(result if 0 < result <= 10 else -1)