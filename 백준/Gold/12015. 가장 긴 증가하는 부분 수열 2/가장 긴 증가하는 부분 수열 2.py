from bisect import bisect_left

n = int(input())
nums = list(map(int, input().split()))

sub = []
for n in nums:
    i = bisect_left(sub, n)
    if i == len(sub):
        sub.append(n)
    else:
        sub[i] = n

print(len(sub))