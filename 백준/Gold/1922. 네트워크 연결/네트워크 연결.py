import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

weights = []
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    weights.append((c, a, b))

root = list(range(N+1))

def union(a, b):
    a_root = find(a)
    b_root = find(b)

    if a_root != b_root:
        if a_root < b_root:
            root[b_root] = a_root
        else:
            root[a_root] = b_root

def find(node):
    if root[node] == node:
        return node

    root[node] = find(root[node])
    return root[node]

total_weight = 0
count = 0
for weight, a, b in sorted(weights):
    if count == N-1:
        break
    if find(a) == find(b):
        continue
    union(a, b)
    total_weight += weight
    count += 1

print(total_weight)
