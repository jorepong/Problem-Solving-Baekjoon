import sys
from collections import defaultdict

n = int(sys.stdin.readline().strip())
pair = int(sys.stdin.readline().strip())

network_map = defaultdict(list)

for _ in range(pair):
    i, j = map(int, sys.stdin.readline().strip().split())
    network_map[i].append(j)
    network_map[j].append(i)

visited = set()
def dfs(num):
    visited.add(num)

    for target in network_map[num]:
        if target not in visited:
            dfs(target)

dfs(1)
print(len(visited)-1)