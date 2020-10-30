def solution(n, costs):
    answer = 0
    union = list(range(n))

    def root(node):
        if node != union[node]:
            union[node] = root(union[node])

        return union[node]

    costs.sort(key = lambda cost: cost[2])
    
    for i1, i2, c in costs:
        root_i1 = root(i1)
        root_i2 = root(i2)

        if root_i1 != root_i2:
            answer += c

            if root_i1 > root_i2:
                union[root_i1] = root_i2

            else:
                union[root_i2] = root_i1

    return answer

print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))
print(solution(6, [[0, 1, 5], [0, 3, 2], [0, 4, 3], [1, 4, 1], [3, 4, 10], [1, 2, 2], [2, 5, 3], [4, 5, 4]]))