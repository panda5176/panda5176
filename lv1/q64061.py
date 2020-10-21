def solution(board, moves):
    answer = 0
    basket = []
    
    for move in moves:
        move -= 1

        for row in board:
            if row[move] != 0:
                basket.append(row[move])

                if len(basket) >= 2 and basket[-1] == basket[-2]:
                        del basket[-1]
                        del basket[-1]
                        answer += 2
            
                row[move] = 0
                break

    return answer