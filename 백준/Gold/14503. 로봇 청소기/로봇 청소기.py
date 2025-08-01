import sys

n, m = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().strip().split())

room = []

for _ in range(n):
    room.append(list(map(int, sys.stdin.readline().strip().split())))

ddx = [-1, 0, 1, 0]
ddy = [0, 1, 0, -1]

count = 0

def check():
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx, ny = r + dx, c + dy
        if 0 <= nx < n and 0 <= ny < m:
            if room[nx][ny] == 0:
                return True
    return False


while True:
    if room[r][c] == 0:
        room[r][c] = 2
        count += 1

    need_cleaning = check()

    if need_cleaning:
        d = (d + 3) % 4
        if room[r + ddx[d]][c + ddy[d]] == 0:
            r += ddx[d]
            c += ddy[d]
    else:
        cd = (d + 2) % 4
        if room[r + ddx[cd]][c + ddy[cd]] != 1:
            r += ddx[cd]
            c += ddy[cd]
        else:
            break

print(count)