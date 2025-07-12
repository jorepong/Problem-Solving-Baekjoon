import sys
from collections import deque
import copy

input = sys.stdin.readline

n, m = map(int, input().split())

lab_map = []
for _ in range(n):
    lab_map.append(list(map(int, input().split())))

empty_spaces = []
virus_list = []
for r in range(n):
    for c in range(m):
        if lab_map[r][c] == 0:
            empty_spaces.append((r, c))
        elif lab_map[r][c] == 2:
            virus_list.append((r, c))

max_safe_area = 0

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs_and_count_safe_area():
    global max_safe_area

    temp_map = copy.deepcopy(lab_map)

    q = deque(virus_list)

    while q:
        r, c = q.popleft()

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            if 0 <= nr < n and 0 <= nc < m and temp_map[nr][nc] == 0:
                temp_map[nr][nc] = 2
                q.append((nr, nc))

    current_safe_area = 0
    for r in range(n):
        for c in range(m):
            if temp_map[r][c] == 0:
                current_safe_area += 1

    max_safe_area = max(max_safe_area, current_safe_area)


def select_walls(wall_count, start_index):
    if wall_count == 3:
        bfs_and_count_safe_area()
        return

    for i in range(start_index, len(empty_spaces)):
        r, c = empty_spaces[i]

        lab_map[r][c] = 1
        select_walls(wall_count + 1, i + 1)
        lab_map[r][c] = 0


select_walls(0, 0)
print(max_safe_area)