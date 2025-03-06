from collections import deque

def solve():
    n, k = map(int, input().split())
    
    if n == k:
        print(0)
        return

    MAX = 100001
    visited = [False] * MAX
    queue = deque([(n, 0)])  # (위치, 시간)

    visited[n] = True

    while queue:
        pos, time = queue.popleft()

        if pos == k:
            print(time)
            return

        # 이동 가능한 세 가지 경우를 탐색
        next_positions = [pos - 1, pos + 1, pos * 2]

        for next_pos in next_positions:
            if 0 <= next_pos < MAX and not visited[next_pos]:
                visited[next_pos] = True
                queue.append((next_pos, time + 1))

solve()