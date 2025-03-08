import sys
from collections import defaultdict

N = int(sys.stdin.readline().strip())
numbers = list(map(int, sys.stdin.readline().strip().split()))

number_map = defaultdict(int)

for index, num in enumerate(sorted(set(numbers))):
    number_map[num] = index

output = [str(number_map[n]) for n in numbers]
print(' '.join(output))