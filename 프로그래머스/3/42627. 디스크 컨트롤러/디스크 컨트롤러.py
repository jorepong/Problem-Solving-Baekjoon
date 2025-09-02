import heapq

def solution(jobs):
    answer = 0
    jobs.sort(key=lambda x: x[0])

    time = 0
    heap = []
    i = 0
    while True:
        while i < len(jobs) and jobs[i][0] <= time:
            heapq.heappush(heap, (jobs[i][1], jobs[i][0], i))
            i += 1

        if heap:
            spend, start, no = heapq.heappop(heap)
            time += spend
            answer += time - start

            if not heap and i >= len(jobs):
                break
        else:
            time += 1

    return int(answer / len(jobs))