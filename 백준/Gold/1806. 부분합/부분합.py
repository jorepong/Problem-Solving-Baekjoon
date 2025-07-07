n, s = map(int, input().split())
nums = list(map(int, input().split()))

p1, p2 = 0, 0
window_length = float('inf')
window_sum = 0

while not (p1 == p2 and p2 == n):
    if p2 == n and window_sum < s:
        break

    if window_sum < s: #윈도우 범위의 합이 s보다 작은 경우
        window_sum += nums[p2]
        p2 += 1
    else: #윈도우 범위의 합이 s보다 큰 경우
        window_length = min(window_length, p2-p1)
        window_sum -= nums[p1]
        p1 += 1
if window_length == float('inf'):
    window_length = 0
print(window_length)