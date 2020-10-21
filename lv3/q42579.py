def solution(genres, plays):
    answer = []

    genres_dic = dict(zip(
        set(genres), [[0, []] for x in range(len(set(genres)))]))
    # print(genres_dic)

    for i in range(len(genres)):
        genres_dic[genres[i]][0] += plays[i]
        genres_dic[genres[i]][1].append([plays[i], i])
    
    genres_dic_sorted = sorted(
        genres_dic.items(), key = lambda t: t[1][0], reverse = True)
    # print(genres_dic_sorted)

    for genre in genres_dic_sorted:
        songs_dic_sorted = sorted(
            genre[1][1], key = lambda t: t[0], reverse = True)
        # print(songs_dic_sorted)

        for song in songs_dic_sorted[:2]:
            answer.append(song[1])
    
    # print(answer, '\n')
    return answer


solution(
    ["classic", "pop", "classic", "classic", "pop"], 
    [500, 600, 150, 800, 2500]
)
solution(
    ["classic", "classic", "classic", "classic", "pop"], 
    [500, 150, 800, 800, 2500]
)
solution(
    ["classic", "classic", "classic", "classic", "pop", "balad"], 
    [150, 800, 800, 500, 2500, 2700]
)
