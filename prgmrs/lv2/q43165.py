def solution(numbers, target):
    from collections import deque
    answer = 0
    queue = deque([(0, -1)])

    while queue:
        sum_previous, idx_previous = queue.popleft()
        idx = idx_previous + 1

        if idx == len(numbers):
            if sum_previous == target:
                answer += 1
            continue

        number = numbers[idx]
        queue.append((sum_previous + number, idx))
        queue.append((sum_previous - number, idx))

    return answer

print(solution([1,1,1,1,1], 3))