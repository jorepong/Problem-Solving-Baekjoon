import sys

N = int(sys.stdin.readline())
board = [[False] * 101 for _ in range(101)]


def draw(d, g):
    if g == 0:
        if d == 0:
            return [(0, 0), (0, 1)]
        elif d == 1:
            return [(0, 0), (-1, 0)]
        elif d == 2:
            return [(0, 0), (0, -1)]
        else:
            return [(0, 0), (1, 0)]

    coords = draw(d, g-1)
    end = coords[-1]

    coords = [(x - end[0], y - end[1]) for x, y in coords]
    for x, y in reversed(list(coords)[:-1]):
        coords.append((y, -x))

    return coords


for _ in range(N):
    y, x, d, g = map(int, sys.stdin.readline().split())
    coords = draw(d, g)
    coords = [(old_x + x - coords[0][0], old_y + y - coords[0][1]) for old_x, old_y in coords]

    for r, c in coords:
        board[r][c] = True


count = 0
for x in range(100):
    for y in range(100):
        if board[x][y] and board[x][y+1] and board[x+1][y] and board[x+1][y+1]:
            count += 1

print(count)
