import sys

n = int(sys.stdin.readline().strip())

count = 0
def dfs(num, target):
    global count
    if num > target:
        return
    elif num == target:
        count += 1

    for i in range(1, 4):
        dfs(num + i, target)

for _ in range(n):
    target = int(sys.stdin.readline().strip())
    count = 0
    dfs(0, target)
    print(count)