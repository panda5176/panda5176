def backpack(jewels, weight_max):
    len_r = len(jewels) + 1
    len_c = weight_max + 1
    dp_table = [[0 for c in range(len_c)] for r in range(len_r)]

    for row in range(len_r):
        for col in range(len_c):
            if row == 0 or col == 0:
                dp_table[row][col] = 0

            v_no_jewel = dp_table[row-1][col]

            if col-jewels[row-1][0] >= 0:
                v_yes_jewel = \
                    dp_table[row-1][col-jewels[row-1][0]] + jewels[row-1][1]

            else:
                v_yes_jewel = 0

            dp_table[row][col] = max(v_yes_jewel, v_no_jewel)
                
    return dp_table[len(jewels)][weight_max]

jewels = [(2, 3), (3, 4), (4, 5), (5, 6)] # (kg, $)
print(backpack(jewels, 10))