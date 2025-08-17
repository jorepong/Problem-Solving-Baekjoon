import sys

n, k = map(int, sys.stdin.readline().split())

dp = [float('inf')] * (k+1)

coins = set()
for _ in range(n):
    coin = int(sys.stdin.readline())
    if coin <= k:
        coins.add(coin)
        dp[coin] = 1
dp[0] = 0

for i in range(1, k+1):
    for coin in coins:
        if i - coin >= 0:
            dp[i] = min(dp[i], dp[i-coin]+1)

print(dp[k] if dp[k] != float('inf') else -1)