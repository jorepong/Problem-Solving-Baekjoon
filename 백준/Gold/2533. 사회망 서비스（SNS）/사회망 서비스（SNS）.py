import sys
sys.setrecursionlimit(10**6 + 10)

def dfs(current_node):
    visited[current_node] = True
    dp[current_node][1] = 1
    dp[current_node][0] = 0

    for next_node in graph[current_node]:
        if not visited[next_node]:
            dfs(next_node)
            dp[current_node][1] += min(dp[next_node][0], dp[next_node][1])
            dp[current_node][0] += dp[next_node][1]

N = int(sys.stdin.readline())
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

dp = [[0, 0] for _ in range(N + 1)]
visited = [False] * (N + 1)

dfs(1)

print(min(dp[1][0], dp[1][1]))