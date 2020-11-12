def solution(number, k):
    answer = ''
    i = 0
    save = False
    save_point = 0
    final_len = len(number) - k

    while True:
        # print(i, k, save, save_point, number)
        if i == len(number)-1:
            answer = number[:final_len]
            return answer

        if number[i] == "9":
            save = False
            i += 1
            continue

        elif save == False:
            save = True
            save_point = i

        if number[i] < number[i+1]:
            number = number[:i] + number[i+1:]
            k -= 1
            i = save_point

            if k == 0:
                answer = number
                return answer

        else:
            i += 1

    return answer

numbers = ["1924", "1231234", "4177252841", "99999815342999215154369999", "1111"]
ks = [2, 3, 4, 8, 2]

for i in range(len(numbers)):
    number = numbers[i]
    k = ks[i]

    print(solution(number, k))