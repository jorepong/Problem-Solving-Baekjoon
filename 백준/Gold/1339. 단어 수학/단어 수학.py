import sys
from collections import defaultdict

N = int(sys.stdin.readline())
words = [sys.stdin.readline().strip() for _ in range(N)]

weights = defaultdict(int)

for word in words:
    num = 1
    for c in reversed(word):
        weights[c] += num
        num *= 10

ans = 0
num = 9
for weight in sorted(weights.values(), reverse=True):
    ans += weight * num
    num -= 1

print(ans)