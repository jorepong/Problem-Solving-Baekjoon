import heapq
import sys

N = int(sys.stdin.readline())

max_heap = []
min_heap = []

for _ in range(N):
    num = int(sys.stdin.readline().strip())
    if len(max_heap) == len(min_heap):
        heapq.heappush(max_heap, -num)
    else:
        heapq.heappush(min_heap, num)

    if min_heap and min_heap[0] < -max_heap[0]:
        temp = -heapq.heappop(max_heap)
        heapq.heappush(min_heap, temp)

        temp = heapq.heappop(min_heap)
        heapq.heappush(max_heap, -temp)

    print(-max_heap[0])