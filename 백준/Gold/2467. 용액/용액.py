import sys

n = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().split()))

start = 0
end = len(nums) - 1

ans = [nums[start], nums[end]]
closest_num = ans[0] + ans[1]

while start < end:
    if nums[start] + nums[end] > 0:
        end -= 1
    elif nums[start] + nums[end] < 0:
        start += 1
    else:
        break

    if start < end and abs(nums[start] + nums[end]) < abs(closest_num):
        closest_num = nums[start] + nums[end]
        ans = [nums[start], nums[end]]

print(*ans)