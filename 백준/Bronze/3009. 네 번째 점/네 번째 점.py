import sys

xs = []
ys = []

for _ in range(3):
    x, y = map(int, sys.stdin.readline().split())
    xs.append(x)
    ys.append(y)

xs.sort()
ys.sort()

ans_x = xs[0] if xs[0] != xs[1] else xs[2]
ans_y = ys[0] if ys[0] != ys[1] else ys[2]
print(ans_x, ans_y)