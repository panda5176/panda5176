def solution(citations):
    answer = 0

    citations = sorted(citations)
    ids = list(range(1, len(citations)+1))[::-1]

    for h, i in zip(citations, ids):
        # print(h, i)
        if h >= i:
            answer = i
            break

    return answer

solution([10, 8, 4, 1, 1])