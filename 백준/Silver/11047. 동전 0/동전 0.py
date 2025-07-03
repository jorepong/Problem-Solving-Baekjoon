n, k = map(int, input().split())

values = []
for _ in range(n):
    values.append(int(input()))

i = 0
while True:
    if i == n-1:
        break

    if values[i] <= k:
        i += 1
    else:
        break

result = 0
for j in range(i, -1, -1):
    result += k // values[j]
    k = k % values[j]

print(result)