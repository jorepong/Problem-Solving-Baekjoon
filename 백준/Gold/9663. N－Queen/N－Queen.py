import sys

N = int(sys.stdin.readline().strip())
board = [[0]*N for _ in range(N)]
count = 0

placed_column = set()

def can_place(x, y):
    for i in range(1, min(x, y)+1):
        if board[y-i][x-i] == 1:
            return False

    for i in range(1, min(N-x-1, y)+1):
        if board[y-i][x+i] == 1:
            return False

    return True


def dfs(y):
    global count
    if y == N:
        count += 1
        return

    for j in range(N):
        if j in placed_column:
            continue
        if can_place(j, y):
            board[y][j] = 1
            placed_column.add(j)
            if y < N:
                dfs(y + 1)
            board[y][j] = 0
            placed_column.remove(j)


dfs(0)
print(count)