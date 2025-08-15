import sys
from collections import defaultdict, deque

n = int(sys.stdin.readline())

a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

sorted_a = sorted(a)
sorted_b = sorted(b)

a_for_b = defaultdict(deque)

for i in range(n):
    a_for_b[sorted_b[i]].append(sorted_a[n-1-i])

ans = 0
for b_num in b:
    ans += b_num * a_for_b[b_num][0]
    a_for_b[b_num].popleft()

print(ans)