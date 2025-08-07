import bisect
import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

lis = []

for num in arr:
    if not lis:
        lis.append(num)
    else:
        if lis[-1] < num:
            lis.append(num)
        else:
            i = bisect.bisect_left(lis, num)
            lis[i] = num

print(len(lis))