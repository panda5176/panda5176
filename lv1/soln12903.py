def solution(s):
    answer = ''
    
    h = len(s) // 2
    
    if len(s)%2 == 1:
        answer = s[h]
    else:
        answer = s[h-1:h+1]
    
    return answer