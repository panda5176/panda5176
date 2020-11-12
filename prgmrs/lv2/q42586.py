def solution(progresses, speeds):
    import math

    answer = []
    day = 0

    for i in range(len(progresses)):
        progress = progresses[i]
        speed = speeds[i]
        new_day = math.ceil((100 - progress) / speed)

        if new_day > day:
            day = new_day
            answer.append(1)

        else:
            answer[-1] += 1

    return answer

# progresses_list = [
#     [40, 93, 30, 55, 60, 65],
#     [93, 30, 55, 60, 40, 65],
#     [5, 5, 5]
# ]
# speeds_list = [
#     [60, 1, 30, 5 , 10, 7],
#     [1, 30, 5 , 10, 60, 7],
#     [21, 25, 20]
# ]
# for j in range(3):
#     print(solution(progresses_list[j], speeds_list[j]))