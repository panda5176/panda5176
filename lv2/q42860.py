def solution(name):
    answer = 0
    t = {
        'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8,
        'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 12, 'P': 11, 'Q': 10,
        'R': 9, 'S': 8, 'T': 7, 'U': 6, 'V': 5, 'W': 4, 'X': 3, 'Y': 2, 'Z': 1
    }
    
    name = list(name)
    answer += t[name[0]]
    name[0] = 'A'
    i = 0

    while True:
        if name.count('A') == len(name):
            break

        count = 1
        count_rev = 1
        f_name = name[i+1:] + name[:i]
        r_name = (name[i+1:] + name[:i])[::-1]

        for n in f_name:
            if n == 'A':
                count += 1
                
            else:
                break
        
        for n in r_name:
            if n == 'A':
                count_rev += 1

            else:
                break
        
        if count <= count_rev:
            i += count
            answer += t[name[i]] + count

        else:
            i -= count_rev
            answer += t[name[i]] + count_rev

        name[i] = 'A'
    
    return answer


names = [
    "JAZ", 
    "JEROEN",
    "JAN", 
    "JANAN", 
    "AAAAA", 
    "BBBAAAB", 
    "ABABAAAAABA"
    ]

for i in range(len(names)):
    name = names[i]
    print(solution(name))
    print('\n###############################################################\n')
    # 11, 9 0 1
    # 56, 9 4 9 12 4 13
    # 23, 9 0 13
    # 38, 9 0 13 0 13
    # 00, 0 0 0 0 0
    # 09, 1 1 1 0 0 0 1
    # 11, 0 1 0 1 0 0 0 1 0