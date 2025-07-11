import sys

r, c = map(int, sys.stdin.readline().split())
board = []

for _ in range(r):
    board.append(list(sys.stdin.readline()))

used_alpha = [False] * 26
used_alpha[ord(board[0][0]) - ord('A')] = True
max_len = 1

def dfs(x, y, count):
    global max_len
    max_len = max(max_len, count)

    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < r and 0 <= ny < c and not used_alpha[ord(board[nx][ny]) - ord('A')]:
            used_alpha[ord(board[nx][ny]) - ord('A')] = True
            dfs(nx, ny, count+1)
            used_alpha[ord(board[nx][ny]) - ord('A')] = False

dfs(0, 0, 1)
print(max_len)