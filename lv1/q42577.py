# def solution(phone_book):
#     answer = True
#     phone_book = sorted(phone_book)

#     for i in range(len(phone_book)):
#         for p1, p2 in zip(phone_book, phone_book[i+1:]):
#             if p2.startswith(p1):
#                 answer = False
#                 return answer

#     return answer

def solution(phone_book):
    answer = True
    hash_map = dict(zip(phone_book, [0] * len(phone_book)))

    for phone_number in phone_book:
        for i in range(len(phone_number)):
            prefix = phone_number[:i+1]

            if prefix != phone_number and prefix in hash_map:
                answer = False
                return answer
                
    return answer

# phone_book_list = [
#     ["119", "97674223", "1195524421"],
#     ["123","456","789"],
#     ["12","123","1235","567","88"]
# ]
# for phone_book in phone_book_list:
#     print(solution(phone_book))