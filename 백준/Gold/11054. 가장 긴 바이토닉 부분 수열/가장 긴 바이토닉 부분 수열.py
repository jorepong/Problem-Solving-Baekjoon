import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

dp = [[1] * n for _ in range(2)]

for i in range(n):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[0][i] = max(dp[0][i], dp[0][j] + 1)
            dp[1][i] = max(dp[1][i], dp[0][i])
        elif arr[j] > arr[i]:
            dp[1][i] = max(dp[1][i], dp[1][j] + 1)

print(max(max(dp[0]), max(dp[1])))