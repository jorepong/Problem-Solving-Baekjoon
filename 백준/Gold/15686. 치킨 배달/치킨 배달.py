n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
chickens = []
houses = []

for i in range(n):
    for j in range(n):
        if board[i][j] == 2:
            chickens.append((i, j))
        elif board[i][j] == 1:
            houses.append((i, j))
            
def find_least_distance(selected_chickens):
    sum_of_least_distance = 0
    for hx, hy in houses:
        least_distance = float('inf')
        for cx, cy in selected_chickens:
            distance = abs(hx-cx) + abs(hy-cy)
            least_distance = min(least_distance, distance)
        sum_of_least_distance += least_distance
    return sum_of_least_distance


final_least_distance = float('inf')
def dfs(index, comp):
    global final_least_distance

    if len(comp) == m:
        least_distance = find_least_distance(comp)
        final_least_distance = min(final_least_distance, least_distance)
        return

    for i in range(index, len(chickens)):
        dfs(i+1, comp+[chickens[i]])

dfs(0, [])
print(final_least_distance)