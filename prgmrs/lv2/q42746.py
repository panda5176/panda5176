def compare(x, y):
    xfirst = int(x + y)
    yfirst = int(y + x)
    # print(xfirst, yfirst)

    return yfirst - xfirst

def solution(numbers):
    from functools import cmp_to_key

    numbers = sorted(list(map(str, numbers)), key = cmp_to_key(compare))
    # print(numbers)
    answer = str(int("".join(numbers)))

    return answer

# numbers = [3, 5, 9, 30, 34]
# print(solution(numbers))