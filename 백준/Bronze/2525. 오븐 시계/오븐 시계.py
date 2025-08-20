import sys

hour, minute = map(int, sys.stdin.readline().split())
required = int(sys.stdin.readline())

minute += required
if minute >= 60:
    hour += minute // 60
    minute %= 60

if hour >= 24:
    hour %= 24

print(hour, minute)