import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

nums.sort()

left, right = 0, N-1
ans = [nums[left], nums[right]]
while left < right:
    if abs(nums[left] + nums[right]) < abs(sum(ans)):
        ans = [nums[left], nums[right]]

    if nums[left] + nums[right] < 0:
        left += 1
    else:
        right -= 1

print(*ans)