import sys
input = sys.stdin.readline

N, M, x, y, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
commands = list(map(int, input().split()))
dice = [0, 0, 0, 0, 0, 0]

dr = [0, 0, 0, -1, 1]
dc = [0, 1, -1, 0, 0]

def roll(d):
    t, b, n, s, e, w = dice
    if d == 1:
        dice[0], dice[1], dice[4], dice[5] = w, e, t, b
    elif d == 2:
        dice[0], dice[1], dice[4], dice[5] = e, w, b, t
    elif d == 3:
        dice[0], dice[1], dice[2], dice[3] = s, n, t, b
    elif d == 4:
        dice[0], dice[1], dice[2], dice[3] = n, s, b, t

r, c = x, y
out_lines = []
for d in commands:
    nr, nc = r + dr[d], c + dc[d]
    if not (0 <= nr < N and 0 <= nc < M):
        continue
    r, c = nr, nc
    roll(d)
    if board[r][c] == 0:
        board[r][c] = dice[1]
    else:
        dice[1] = board[r][c]
        board[r][c] = 0
    out_lines.append(str(dice[0]))

print("\n".join(out_lines))
