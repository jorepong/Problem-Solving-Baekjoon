import sys

nums = set()

for _ in range(10):
    nums.add(int(sys.stdin.readline()) % 42)

print(len(nums))