import sys

n = int(sys.stdin.readline().strip())

outputs = []
count = 0
def move(start, to, temp, num):
    global count

    if num == 1:
        count += 1
        outputs.append((start, to))
        return

    move(start, temp, to, num - 1)
    move(start, to, temp, 1)
    move(temp, to, start, num - 1)

move(1, 3, 2, n)

print(count)
for output in outputs:
    print(*output)