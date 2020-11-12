def solution(numbers):
    from itertools import permutations
    from math import sqrt

    answer = 0
    permutes = []
    
    for i in range(1, len(numbers)+1):
        permutes_str = list(permutations(sorted(list(list(numbers))), i))
        permutes += list(map(int, list(map(''.join, permutes_str))))

    permutes = sorted(set(permutes))
    # print(permutes)

    for p in permutes:
        if p == 0 or p == 1:
            continue
        
        undivided = True

        for j in range(2, int(sqrt(p))+1):
            if p%j == 0:
                undivided = False
                break
        
        if undivided:
            answer += 1
        
    return answer

# numbers_list = ["12", "17", "011"]
# for numbers in numbers_list:
#     print(solution(numbers))