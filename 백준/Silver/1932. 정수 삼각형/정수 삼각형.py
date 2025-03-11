import sys

N = int(sys.stdin.readline().strip())
triangle = []

for _ in range(N):
    triangle.append(list(map(int, sys.stdin.readline().strip().split())))

dp = [triangle[0]]

for i in range(1, N):
    line = []
    for j in range(i+1):
        if j==0:
            line.append(dp[i-1][j] + triangle[i][j])
        elif i==j:
            line.append(dp[i-1][j-1] + triangle[i][j])
        else:
            line.append(max(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j])
    dp.append(line)

print(max(dp[-1]))