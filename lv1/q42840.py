def solution(answers):
    answer = []
    man1 = [1, 2, 3, 4, 5]
    man2 = [2, 1, 2, 3, 2, 4, 2, 5]
    man3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    points = [0, 0, 0]
    
    for i, a in enumerate(answers):
        if a == man1[i % 5]:
            points[0] += 1

        if a == man2[i % 8]:
            points[1] += 1
            
        if a == man3[i % 10]:
            points[2] += 1
    
    m = max(points)
    
    for j in range(3):
        if points[j] == m:
            answer.append(j+1)
    
    return answer