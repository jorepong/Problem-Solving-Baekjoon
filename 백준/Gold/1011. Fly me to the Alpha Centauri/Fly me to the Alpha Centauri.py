import sys

t = int(sys.stdin.readline())

for _ in range(t):
    x, y = map(int, sys.stdin.readline().split())
    distance = y - x
    answer = 0

    i = 1
    while True:
        count = min(2, distance // i)
        distance -= count * i
        answer += count
        if count <= 1:
            break
        i += 1

    if distance > 0:
        answer += 1
    print(answer)