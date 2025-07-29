import sys

n = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().split()))

start = 0
end = len(nums) - 1

ans = [nums[start], nums[end]]
closest_num = ans[0] + ans[1]

while start + 1 != end:
    if abs(nums[start + 1] + nums[end]) < abs(nums[start] + nums[end - 1]):
        start += 1
    elif abs(nums[start + 1] + nums[end]) >= abs(nums[start] + nums[end - 1]):
        end -= 1

    if abs(nums[start] + nums[end]) < abs(closest_num):
        closest_num = nums[start] + nums[end]
        ans = [nums[start], nums[end]]

print(*ans)