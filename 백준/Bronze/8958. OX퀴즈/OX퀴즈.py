import sys

t = int(sys.stdin.readline())

for _ in range(t):
    results = sys.stdin.readline()
    score = count = 0
    for result in results:
        count = count + 1 if result == 'O' else 0
        score += count
    print(score)