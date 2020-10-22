def solution(triangle):
    answer = 0
    depth = len(triangle)
    table = [[0 for x in range(depth+1)] for x in range(depth+1)]
    bottom = []

    for i in range(depth):
        for j in range(len(triangle[i])):
            table[i+1-j][j+1] = triangle[i][j] + max(
                table[i+1-j][j], table[i-j][j+1]
            )

            if i == depth-1:
                bottom.append(table[i+1-j][j+1])

    answer = max(bottom)

    return answer

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
