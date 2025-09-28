import sys

sys.setrecursionlimit(110000)
input = sys.stdin.readline


def solve():
    n = int(input())
    choices = [0] + list(map(int, input().split()))

    visited = [False] * (n + 1)
    member_num = 0
    for i in range(1, n + 1):
        path = []
        curr = i

        team_members = set()

        while not visited[curr]:
            visited[curr] = True
            path.append(curr)
            team_members.add(curr)
            curr = choices[curr]

        if curr in team_members:
            index = path.index(curr)
            member_num += len(path) - index

    print(n - member_num)


T = int(input())
for _ in range(T):
    solve()