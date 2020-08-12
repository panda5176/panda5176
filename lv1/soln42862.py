def solution(n, lost, reserve):
    answer = 0
    lost_set = set(lost) - set(reserve)
    reserve_set = set(reserve) - set(lost)
    
    for r in reserve_set:
			
        if r-1 in lost_set:
            lost_set.remove(r-1)

        elif r+1 in lost_set:
            lost_set.remove(r+1)
			
    answer = n - len(lost_set)

    return answer