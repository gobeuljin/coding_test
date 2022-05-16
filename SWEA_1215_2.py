def rot_list(l):
    a = len(l) # 행 길이
    b = len(l[0]) # 열 길이

    rotated_list = [[0]*a for _ in range(b)]

    for i in range(a):
        for j in range(b):
            rotated_list[j][a-i-1] = l[i][j]
    
    return rotated_list

for t in range(1, 11):
    N = int(input()) # 회문길이
    word_table = [list(map(str, input())) for _ in range(8)]
    rot_word_table = word_table.copy()

    rot_word_table = rot_list(rot_word_table)
    rot_word_table = rot_list(rot_word_table) # 총 180 도 회전

    cnt = 0
    for i in range(8): # 행 비교
        for j in range(8 -N +1):
            if word_table[i][j:j+N] == rot_word_table[-(i+1)][-j+(8-N):-j+8]:
                cnt += 1

    word_table = rot_list(word_table) # 열 비교를 위한 회전
    rot_word_table = rot_list(rot_word_table)

    for i in range(8): # 열 비교
        for j in range(8 -N +1):
            if word_table[i][j:j+N] == rot_word_table[-(i+1)][-j+(8-N):-j+8]:
                cnt += 1
            
    print("#{} {}".format(t, cnt))