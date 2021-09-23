def solution(scoville, K):
    import heapq

    answer = 0
    heapq.heapify(scoville)

    while True:
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        mixed = first + second * 2

        heapq.heappush(scoville, mixed)
        smallest = scoville[0]
        answer += 1

        # print(scoville)

        if smallest >= K:
            break

        if len(scoville) == 1:
            answer = -1
            break

    return answer

# print(solution([1, 2, 3, 9, 10, 12], 7))
# print(solution([1, 2, 3], 14))