import sys

n, k = map(int, sys.stdin.readline().split())

dp = [[-1] * (k + 1) for _ in range(n + 1)]

def dfs(target, remain):
    if remain == 1:
        dp[target][remain] = 1
    elif dp[target][remain] == -1:
        dp[target][remain] = 0
        for i in range(0, target + 1):
            dp[target][remain] += dfs(target - i, remain - 1)

    return dp[target][remain]

print(dfs(n, k) % 1000000000)