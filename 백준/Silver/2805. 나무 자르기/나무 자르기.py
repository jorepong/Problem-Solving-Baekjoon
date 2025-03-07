import sys


def solve():
    N, M = map(int, sys.stdin.readline().strip().split())
    trees = list(map(int, sys.stdin.readline().strip().split()))

    left, right = 0, max(trees)
    answer = float('inf')

    while left <= right:
        mid = (left + right) // 2
        total_wood = sum(tree - mid for tree in trees if tree > mid)

        if total_wood < M:
            right = mid - 1
        else:
            answer = mid
            left = mid + 1

    print(answer)

solve()