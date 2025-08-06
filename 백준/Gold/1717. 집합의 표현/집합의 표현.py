import sys

sys.setrecursionlimit(10**6)

n, m = map(int, sys.stdin.readline().split())
root = list(range(n+1))

def union(a, b):
    a_root = find(a)
    b_root = find(b)

    if a_root != b_root:
        if a_root < b_root:
            root[b_root] = a_root
        else:
            root[a_root] = b_root

def find(a):
    if root[a] == a:
        return a
    else:
        root[a] = find(root[a])
        return root[a]

def is_same_root(a, b):
    a_root = find(a)
    b_root = find(b)

    return a_root == b_root

for _ in range(m):
    o, a, b = map(int, sys.stdin.readline().split())

    if o == 0:
        union(a, b)
    else:
        if is_same_root(a, b):
            print('YES')
        else:
            print('NO')