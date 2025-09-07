import sys

sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())
parents = list(map(int, sys.stdin.readline().split()))
node_to_delete = int(sys.stdin.readline())

adj = [[] for _ in range(n)]
root = -1
for i, p in enumerate(parents):
    if p == -1:
        root = i
    else:
        adj[p].append(i)

leaf_count = 0

def dfs(node):
    global leaf_count
    
    if node == node_to_delete:
        return

    num_valid_children = 0
    if adj[node]:
        for child in adj[node]:
            if child != node_to_delete:
                num_valid_children += 1
                dfs(child)
    
    if num_valid_children == 0:
        leaf_count += 1

if root == node_to_delete:
    print(0)
else:
    dfs(root)
    print(leaf_count)