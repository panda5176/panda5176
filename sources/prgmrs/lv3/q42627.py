def solution(jobs):
    import heapq
    answer, end_time = 0, 0
    len_jobs = len(jobs)

    jobs.sort()
    heapq.heapify(jobs)
    next_jobs = []
    heapq.heapify(next_jobs)
    
    while jobs:
        i = 0

        while jobs:
            start, time = jobs[i]

            if start <= end_time:
                heapq.heappush(next_jobs, [time, start])
                heapq.heappop(jobs)

            else:
                break
        
        if next_jobs:
            time, start = heapq.heappop(next_jobs)
            answer += end_time - start + time
            end_time += time

        else:
            end_time += 1
            continue

        while next_jobs:
            time, start = heapq.heappop(next_jobs)
            heapq.heappush(jobs, [start, time])

    answer = answer // len_jobs

    return answer
