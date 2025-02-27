import sys

n, m = map(int, sys.stdin.readline().strip().split(' '))
cards = list(map(int, sys.stdin.readline().strip().split(' ')))

best = 0

for i in range(len(cards) - 2):
    for j in range(i+1, len(cards) - 1):
        for k in range(j+1, len(cards)):
            if best < cards[i] + cards[j] + cards[k] <= m:
                best = cards[i] + cards[j] + cards[k]

print(best)