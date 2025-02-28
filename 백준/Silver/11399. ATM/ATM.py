import sys

n = int(sys.stdin.readline().strip())
times = list(map(int, sys.stdin.readline().strip().split()))
times.sort()

total_sum = 0
sum = 0

for time in times:
    sum += time
    total_sum += sum

print(total_sum)