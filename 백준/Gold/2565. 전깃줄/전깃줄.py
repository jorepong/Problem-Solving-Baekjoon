import sys

n = int(sys.stdin.readline())

lines = []
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    lines.append((a, b))

lines.sort()

b_points = []
for line in lines:
    b_points.append(line[1])

dp = [1] * n

for i in range(n):
    for j in range(i):
        if b_points[j] < b_points[i]:
            dp[i] = max(dp[i], dp[j] + 1)

result = n - max(dp)
print(result)