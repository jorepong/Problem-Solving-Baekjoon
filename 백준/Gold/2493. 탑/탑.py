import sys

n = int(sys.stdin.readline())
tops = list(map(int, sys.stdin.readline().split()))

stack = []
answer = [0] * n

for i in range(n-1, -1, -1):
    while stack and tops[stack[-1]] < tops[i]:
        answer[stack.pop()] = i+1
    stack.append(i)

print(*answer)