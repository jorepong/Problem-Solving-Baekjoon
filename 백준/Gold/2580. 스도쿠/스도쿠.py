import sys

zeros = []
board = []

for i in range(9):
    row = list(map(int, sys.stdin.readline().split()))
    for j, n in enumerate(row):
        if n == 0:
            zeros.append((i, j))
    board.append(row)

def check(position, n):
    x, y = zeros[position]
    for i in range(9):
        if board[x][i] == n:
            return False
        if board[i][y] == n:
            return False

    for i in range(3):
        for j in range(3):
            if board[(x // 3) * 3 + i][(y // 3) * 3 + j] == n:
                return False

    return True

def dfs(index):
    if index == len(zeros):
        for row in board:
            print(*row)
        return True

    for n in range(1, 10):
        if check(index, n):
            x, y = zeros[index]
            board[x][y] = n
            if dfs(index+1):
                return True
            board[x][y] = 0

    return False

dfs(0)