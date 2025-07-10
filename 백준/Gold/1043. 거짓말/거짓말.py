from collections import defaultdict, deque

n, m = map(int, input().split())

poisoned_member = [False] * (n+1)
poisoned_member_init = list(map(int, input().split()))[1:]

graph = defaultdict(set)
parties = []

for i in range(1, m+1):
    party = list(map(int, input().split()))[1:]
    parties.append(party)

    for p1 in range(0, len(party)-1):
        for p2 in range(p1+1, len(party)):
            graph[party[p1]].add(party[p2])
            graph[party[p2]].add(party[p1])

def bfs(start):
    queue = deque([start])

    while queue:
        item = queue.popleft()
        poisoned_member[item] = True

        for p in graph[item]:
            if not poisoned_member[p]:
                queue.append(p)

for init_member in poisoned_member_init:
    if not poisoned_member[init_member]:
        bfs(init_member)

count = 0
for party in parties:
    is_poisoned = False
    for party_member in party:
        if poisoned_member[party_member]:
            is_poisoned = True
            break
    if not is_poisoned:
        count += 1

print(count)