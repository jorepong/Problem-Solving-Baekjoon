import sys

N, M = map(int, sys.stdin.readline().strip().split())
nums = list(map(int, sys.stdin.readline().strip().split()))

prefix_sum = [0] * (N+1)

for i in range(1, N+1):
    prefix_sum[i] = prefix_sum[i-1] + nums[i-1]

for _ in range(M):
    i, j = map(int, sys.stdin.readline().strip().split())
    print(prefix_sum[j] - prefix_sum[i-1])