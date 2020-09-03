def solution(brown, yellow):
    from math import ceil

    answer = []
    w_plus_h = int(brown/2) - 2 # 3 2 10 

    for w in range(ceil(w_plus_h/2), w_plus_h): # 2-2 1-1 5-9
        h = w_plus_h - w
        if yellow == h * w:
            answer = [w+2, h+2]

    return answer

browns = [10, 8, 24]
yellows = [2, 1, 24]

for i in range(3):
    brown = browns[i]
    yellow = yellows[i]

    print(solution(brown, yellow))