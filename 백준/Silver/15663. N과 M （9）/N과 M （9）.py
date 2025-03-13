import sys

N, M = map(int, sys.stdin.readline().strip().split())
nums = list(map(int, sys.stdin.readline().strip().split()))
result = set()

def dfs(path, used, remain):
    if remain == 0:
        result.add(tuple(path))
        return

    for index, state in enumerate(used):
        if not state:
            used[index] = True
            dfs(path + [nums[index]], used, remain-1)
            used[index] = False

dfs([], [False] * N, M)
result = sorted(list(result))

for item in result:
    print(*item)