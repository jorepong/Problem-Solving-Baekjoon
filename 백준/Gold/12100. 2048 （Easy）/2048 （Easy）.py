from copy import deepcopy
import sys

sys.setrecursionlimit(10**6)

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

def move(board, dx, dy):
    if dx != 0: #행간 비교
        for r in range(n): # 한 행씩 비교해나간다.
            new_line = [] # 업데이트 될 리스트
            last_update = False
            for i in range(n): # 한쪽 끝에서부터 반대쪽 끝까지 반복한다.
                target_index = i if dx == -1 else n-1-i
                if new_line and new_line[-1] == board[r][target_index] and not last_update:
                    new_line[-1] = board[r][target_index] * 2
                    last_update = True
                elif board[r][target_index] != 0:
                    new_line.append(board[r][target_index])
                    last_update = False
            for _ in range(n - len(new_line)):
                new_line.append(0)
            board[r] = new_line if dx == -1 else new_line[::-1]
    else: #열간 비교
        for c in range(n):
            new_line = []
            last_update = False
            for i in range(n):
                target_index = i if dy == -1 else n-1-i
                if new_line and new_line[-1] == board[target_index][c] and not last_update:
                    new_line[-1] = board[target_index][c] * 2
                    last_update = True
                elif board[target_index][c] != 0:
                    new_line.append(board[target_index][c])
                    last_update = False
            for _ in range(n - len(new_line)):
                new_line.append(0)
            new_line = new_line if dy == -1 else new_line[::-1]
            for i in range(n):
                board[i][c] = new_line[i]


ans = -float('inf')
def find_max_num(board):
    global ans
    for row in board:
        ans = max(ans, max(row))

def dfs(board, count):
    find_max_num(board)

    if count == 5:
        return

    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        target_board = deepcopy(board)
        move(target_board, dx, dy)
        if target_board == board:
            continue
        dfs(target_board, count + 1)

dfs(board, 0)
print(ans)