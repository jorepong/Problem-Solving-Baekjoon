import bisect
import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
nge = [-1] * n
stack = []

for i in range(n):
    while stack and nums[stack[-1]] < nums[i]:
        nge[stack.pop()] = nums[i]
    stack.append(i)

print(*nge)