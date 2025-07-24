import sys

sys.setrecursionlimit(10**6)

n, k = map(int, sys.stdin.readline().split())
values = []
for _ in range(n):
    values.append(int(sys.stdin.readline().strip()))

dp = [0] * (k + 1)
dp[0] = 1

for value in values:
    for i in range(value, k + 1):
        dp[i] += dp[i - value]

print(dp[k])