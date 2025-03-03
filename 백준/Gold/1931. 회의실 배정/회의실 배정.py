import sys

n = int(sys.stdin.readline().strip())

times = []

for _ in range(n):
    start, end = map(int, sys.stdin.readline().strip().split())
    times.append((start, end))

times.sort()

last_meeting_start = times[0][0]
last_meeting_end = times[0][1]
count = 1

for time in times[1:]:
    if time[0] >= last_meeting_end:
        last_meeting_start = time[0]
        last_meeting_end = time[1]
        count += 1
    elif last_meeting_start <= time[0] and last_meeting_end >= time[1]:
        last_meeting_start = time[0]
        last_meeting_end = time[1]

print(count)