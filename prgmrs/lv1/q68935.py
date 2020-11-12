def ternary(n):
    q = n//3
    r = n%3

    if q == 0:
        return str(r)

    else:
        return ternary(q) + str(r)

def solution(n):
    answer = int(ternary(n)[::-1], 3)
    
    return answer