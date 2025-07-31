import sys
from collections import deque

n = int(sys.stdin.readline())

board = [[0] * n for _ in range(n)]

for _ in range(int(sys.stdin.readline())):
    x, y = map(int, sys.stdin.readline().split())
    board[x - 1][y - 1] = 1 # 사과의 위치

move = deque()
player = deque([(0, 0)])
board[0][0] = 2

for _ in range(int(sys.stdin.readline())):
    x, c = sys.stdin.readline().split()
    move.append((x, c))

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
time = 0
i = 0
while True:
    time += 1

    cx, cy = player[-1]
    nx, ny = cx + directions[i][0], cy + directions[i][1]

    if not (0 <= nx < n and 0 <= ny < n): # 게임 보드를 벗어난 경우
        break

    if board[nx][ny] == 2: # 자신과 부딪힌 경우
        break
    elif board[nx][ny] == 1: # 사과와 만난 경우
        pass
    else:
        x, y = player.popleft()
        board[x][y] = 0

    board[nx][ny] = 2
    player.append((nx, ny))

    if move and int(move[0][0]) == time:
        _, direction = move.popleft()
        if direction == 'L':
            i = (i + 3) % 4
        else:
            i = (i + 1) % 4

print(time)