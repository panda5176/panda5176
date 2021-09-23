def solution(numbers):
    answer = []
    
    for i in range(len(numbers)-1):
        n1 = numbers[i]
        
        for j in range(1, len(numbers)-i):
            n2 = numbers[i+j]
            answer.append(n1+n2)
            
    answer = sorted(list(set(answer)))
    
    return answer