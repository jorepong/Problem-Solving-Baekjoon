import sys

nums = list(map(int, sys.stdin.readline().split()))
nums.sort()

if nums[0] == nums[2]:
    print(10000 + nums[0] * 1000)
elif nums[0] != nums[1] and nums[1] != nums[2]:
    print(nums[2] * 100)
else:
    print(1000 + nums[1] * 100)