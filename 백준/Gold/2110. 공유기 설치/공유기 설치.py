import sys

n, c = map(int, sys.stdin.readline().split())
houses = []

for _ in range(n):
    houses.append(int(sys.stdin.readline()))

houses.sort()

def check(distance):
    count = 1
    i = 1
    last_i = 0
    while i < len(houses):
        if houses[i] >= houses[last_i] + distance:
            count += 1
            last_i = i
        i += 1

    return count >= c


start = 1
end = houses[-1] - houses[0]
answer = 0

while start <= end:
    mid = (start + end) // 2
    if check(mid):
        answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)