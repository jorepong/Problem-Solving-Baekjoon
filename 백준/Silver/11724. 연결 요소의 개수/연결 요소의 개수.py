#연결 요소의 개수 
import sys 
input = sys.stdin.readline
sys.setrecursionlimit(10**6)  # 재귀 깊이 증가 

N, M = map(int, input().split()) #정점 개수, 간선 개수 

def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if visited[i]==False: 
            dfs(graph, i, visited)



# 그래프 입력 (adjacency list 방식)
graph = [[] for _ in range(N + 1)] 
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (N+1)
cnt = 0

for i in range(1, N + 1):
    if visited[i]==False:
        dfs(graph, i, visited)
        cnt += 1
 
print(cnt)

