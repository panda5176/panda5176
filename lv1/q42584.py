# def solution(prices):
#     answer = []
#     len_prices = len(prices)

#     for i in range(len_prices):
#         price = prices[i]

#         for j in range(len_prices - i - 1):
#             price_future = prices[i + j + 1]

#             if price > price_future:
#                 answer.append(j+1)
#                 break

#             if i+j+2 == len_prices:
#                 answer.append(len_prices - i - 1)
    
#     answer.append(0)

#     return answer

def solution(prices):
    answer = [0] * len(prices)
    stack = [[-1,-1]]

    for i in range(len(prices)):
        price = prices[i]

        if price < stack[-1][1]:
            for j, former_price in stack[::-1]:
                if price < former_price:
                    answer[j] = i - j
                    del stack[-1]
                
                else:
                    break
        
        stack.append([i, price])
    
    for k, remain_price in stack[1:]:
        answer[k] = len(prices) - k - 1

    return answer

prices = [1,2,3,2,3]
print(solution(prices))
