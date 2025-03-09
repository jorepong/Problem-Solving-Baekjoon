import sys

n = int(sys.stdin.readline().strip())

dp = [float('inf')] * 5000
dp[2] = 1
dp[4] = 1

for i in range(5, n):
    a = dp[i-3]
    b = dp[i-5]

    dp[i] = min(a, b) + 1

answer = dp[n-1] if dp[n-1] != float('inf') else -1
print(answer)