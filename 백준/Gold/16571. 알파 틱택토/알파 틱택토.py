import sys
from copy import deepcopy
from enum import Enum, auto


class State(Enum):
    lose = auto()
    draw = auto()
    win = auto()
    yet = auto()

def decide_board_state(board):
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]: # 대각선인 경우 1
        if board[0][0] == my:
            return State.win
        elif board[0][0] == op:
            return State.lose

    if board[2][0] == board[1][1] and board[1][1] == board[0][2]: # 대각선인 경우 2
        if board[2][0] == my:
            return State.win
        elif board[2][0] == op:
            return State.lose

    for i in range(3):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2]:
            if board[i][0] == my:
                return State.win
            elif board[i][0] == op:
                return State.lose

    for i in range(3):
        if board[0][i] == board[1][i] and board[1][i] == board[2][i]:
            if board[0][i] == my:
                return State.win
            elif board[0][i] == op:
                return State.lose

    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return State.yet

    return State.draw

def dfs(board, is_my_turn):
    board_state = decide_board_state(board)
    if board_state != State.yet:
        return board_state

    final_result = -float('inf') if is_my_turn else float('inf')
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                new_board = deepcopy(board)
                new_board[i][j] = my if is_my_turn else op
                result = dfs(new_board, not is_my_turn)
                if is_my_turn:
                    final_result = max(final_result, result.value)
                else:
                    final_result = min(final_result, result.value)

    return State(final_result)

def get_my_player(board):
    player_one = 0
    player_two = 0

    for i in range(3):
        for j in range(3):
            if board[i][j] == 1:
                player_one += 1
            elif board[i][j] == 2:
                player_two += 1

    if player_one == player_two:
        return 1
    else:
        return 2


board = []
for _ in range(3):
    board.append(list(map(int, sys.stdin.readline().strip().split())))

my = get_my_player(board)
op = 3 - my # 내가 1이면 상대는 2, 내가 2면 상대는 1

result = dfs(board, True)
if result == State.win:
    print('W')
elif result == State.lose:
    print('L')
elif result == State.draw:
    print('D')