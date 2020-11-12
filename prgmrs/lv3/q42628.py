def solution(operations):
    import heapq

    answer = []
    dhq = []
    heapq.heapify(dhq)

    for operation in operations:

        if operation.split()[0] == "I":
            heapq.heappush(dhq, int(operation.split()[1]))

        else:
            if dhq == []:
                continue

            elif operation.split()[1] == "1":
                dhq.pop(dhq.index(max(dhq)))
                heapq.heapify(dhq)

            else:
                heapq.heappop(dhq)

        # print(dhq)
    
    if dhq == []:
        answer = [0,0]
        
    else:
        answer = [dhq.pop(dhq.index(max(dhq))), heapq.heappop(dhq)]

    return answer

print(solution(["I 16","D 1", "D 1"]))
print(solution(["I 7","I 5","I -5","D -1"]))