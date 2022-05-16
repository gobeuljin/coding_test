
## 2차원 배열 시계방향으로 90도 회전 ##
# https://choichumji.tistory.com/74 #
def rot_list(l):
    a = len(l) # 행 길이
    b = len(l[0]) # 열 길이

    rotated_list = [[0]*a for _ in range(b)]

    for i in range(a):
        for j in range(b):
            rotated_list[j][a-i-1] = l[i][j]
    
    return rotated_list