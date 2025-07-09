n, k = map(int, input().split())
nums = list(map(int, input().split()))

window_sum = sum(nums[:k])
answer = window_sum
i = 0

while i < n - k:
    window_sum -= nums[i]
    window_sum += nums[i+k]
    answer = max(answer, window_sum)
    i += 1

print(answer)