import heapq
import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())

heap = []
for _ in range(m):
    data = list(map(int, input().split()))
    heapq.heappush(heap, (data[2], data[0], data[1]))

parent = list(range(0, n+1))

def find(v):
    if v == parent[v]:
        return v
    else:
        parent[v] = find(parent[v])
        return parent[v]

def union(v1, v2):
    p1 = find(v1)
    p2 = find(v2)

    if p1 != p2:
        if p1 < p2:
            parent[p2] = v1
        else:
            parent[p1] = p2
        return True
    return False

answer = 0

while heap:
    w, s, e = heapq.heappop(heap)
    if union(s, e):
        answer += w

print(answer)