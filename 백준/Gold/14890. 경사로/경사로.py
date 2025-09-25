import sys

N, L = map(int, sys.stdin.readline().strip().split())
board = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

path = 0

for row in range(N):
    available_block = 1

    for i in range(1, N):
        if board[row][i-1] == board[row][i]:
            available_block += 1
        elif abs(board[row][i-1] - board[row][i]) == 1:
            if board[row][i-1] > board[row][i] and available_block >= 0:
                available_block = -(L-1)
            else:
                if available_block >= L:
                    available_block = 1
                else:
                    available_block = -1
                    break
        else:
            available_block = -1
            break

    if available_block >= 0:
        path += 1

for col in range(N):
    available_block = 1

    for i in range(1, N):
        if board[i - 1][col] == board[i][col]:
            available_block += 1
        elif abs(board[i - 1][col] - board[i][col]) == 1:
            if board[i - 1][col] > board[i][col] and available_block >= 0:
                available_block = -(L-1)
            else:
                if available_block >= L:
                    available_block = 1
                else:
                    available_block = -1
                    break
        else:
            available_block = -1
            break

    if available_block >= 0:
        path += 1

print(path)