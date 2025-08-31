import sys

wheels = [list(map(int, input())) for _ in range(4)]

def rotate(index, di):
    if di == 1:
        wheels[index] = [wheels[index][-1]] + wheels[index][0:7]
    else:
        wheels[index] = wheels[index][1:] + [wheels[index][0]]

for _ in range(int(sys.stdin.readline())):
    num, direction = map(int, sys.stdin.readline().split())
    num -= 1
    if direction == -1:
        direction = 0

    rotatable_position = [False] * 3

    for i in range(3):
        if wheels[i][2] != wheels[i+1][6]:
            rotatable_position[i] = True

    d = 1 - direction
    for i in range(num, 0, -1):
        p = (i + (i-1)) // 2
        if rotatable_position[p]:
            rotate(i-1, d)
            d = 1 - d
        else:
            break

    d = 1 - direction
    for i in range(num, 3):
        p = (i + (i+1)) // 2
        if rotatable_position[p]:
            rotate(i+1, d)
            d = 1 - d
        else:
            break

    rotate(num, direction)

score = 0
for i in range(4):
    if wheels[i][0] == 1:
        score += 2**i

print(score)