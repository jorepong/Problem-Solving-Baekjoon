import sys
from collections import defaultdict, deque

t = int(sys.stdin.readline().strip()) # 테스트 케이스

for _ in range(t):
    n, k = map(int, sys.stdin.readline().strip().split()) # n: 건물 개수, k: 건설 순서 규칙 개수
    times = [0] + list(map(int, sys.stdin.readline().strip().split())) # 건물당 건설 시간

    graph = defaultdict(list) # 그래프 정보
    in_degree = [0] * (n+1) # 진입 차수 카운트

    for _ in range(k):
        v1, v2 = map(int, sys.stdin.readline().strip().split())
        graph[v1].append(v2)
        in_degree[v2] += 1 # 진입 차수를 카운트 한다.

    target = int(sys.stdin.readline().strip()) # 목표 건물

    queue = deque([i for i, v in enumerate(in_degree) if v == 0 and i != 0])
    dp = times.copy()

    while queue:
        item = queue.popleft()

        for v in graph[item]:
            in_degree[v] -= 1
            dp[v] = max(dp[v], times[v] + dp[item])
            if in_degree[v] == 0:
                queue.append(v)

    print(dp[target])