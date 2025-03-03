import sys

dp = [0, 1, 2]
n = int(sys.stdin.readline().strip())

def get_num(n):
    if len(dp) - 1 < n:
        for i in range(len(dp), n+1):
            dp.append(dp[i-1] + dp[i-2])

    return dp[n]

print(get_num(n) % 10007)