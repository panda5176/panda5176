def solution(clothes):
    cat_hash = {}

    for cloth in clothes:
        if cloth[1] in cat_hash:
            cat_hash[cloth[1]] += 1

        else:
            cat_hash[cloth[1]] = 1

    answer = 1

    for cat in cat_hash:
        answer *= cat_hash[cat]+1
    
    answer -= 1

    return answer

# clothes_list = [
#     [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], \
#         ["green_turban", "headgear"]],
#     [["crow_mask", "face"], ["blue_sunglasses", "face"], \
#         ["smoky_makeup", "face"]]
# ]
# for clothes in clothes_list:
#     print(solution(clothes))