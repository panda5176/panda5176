def solution(people, limit):
    answer = 0
    people.sort() # reverse = True consumes time
    f_index = 0
    r_index = 1

    while True:
        # print(people[f_index], people[-r_index])
        answer += 1
        light = people[f_index] # pop(0) = O(N)
        heavy = people[-r_index]
        r_index += 1
        if light + heavy <= limit:
            f_index += 1
        if f_index + r_index > len(people):
            break
        
    return answer

people = [70, 80, 50]
limit = 100
print(solution(people, limit))