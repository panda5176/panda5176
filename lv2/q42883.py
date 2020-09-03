def solution(number, k):
    answer = ''

    count = 0
    for kk in range(k):
        for i in range(len(number)):
            if number[i] < number[i+1]:
                # print(number, " yes")
                number = number[:i] + number[i+1:]
                count += 1
                
                if count == k:
                    answer = number
                    return answer
                
                break
                
            # else:
            #     print(number, " no")

    return answer

numbers = ["1924", "1231234", "4177252841"]
ks = [2, 3, 4]

for i in range(3):
    number = numbers[i]
    k = ks[i]

    print(solution(number, k))