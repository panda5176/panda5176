def solution(priorities, location):
    answer = 0
    ids = list(range(len(priorities)))

    while True:
        q = priorities.pop(0)
        i = ids.pop(0)
        printing = True

        for p in priorities:
            if p > q:
                priorities.append(q)
                ids.append(i)
                printing = False
                break

        if printing == True:
            answer += 1

            if i == location:
                return answer

        # print(priorities, ids)

    return answer

# priorities = [2,1,3,2]
# location = 2
# print(solution(priorities, location))