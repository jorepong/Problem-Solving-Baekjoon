import sys

N = int(sys.stdin.readline().strip())

house = [[0] * 3 for _ in range(N)]

for i in range(N):
    r, g, b = map(int, sys.stdin.readline().strip().split())
    if i == 0:
        house[0][0], house[0][1], house[0][2] = r, g, b
    else:
        house[i][0] = min(house[i-1][1], house[i-1][2]) + r
        house[i][1] = min(house[i-1][0], house[i-1][2]) + g
        house[i][2] = min(house[i-1][0], house[i-1][1]) + b

answer = min(house[-1])
print(answer)