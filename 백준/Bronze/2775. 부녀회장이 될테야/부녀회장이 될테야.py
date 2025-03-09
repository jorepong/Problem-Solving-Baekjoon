import sys

T = int(sys.stdin.readline().strip())
dp = [[1] * 15 for _ in range(15)]
dp[0] = list(range(16))

for k in range(1, 15):
    for n in range(1, 15):
        if n == 1:
            dp[k][n] = dp[k-1][n]
        else:
            dp[k][n] = dp[k][n-1] + dp[k-1][n]

for _ in range(T):
    k = int(sys.stdin.readline().strip())
    n = int(sys.stdin.readline().strip())
    print(dp[k][n])