for t in range(1, 11):
    N = int(input()) # 회문길이
    #word_table = [list(map(str, input())) for _ in range(8)]
    word_table = [list(input()) for _ in range(8)]
    cnt = 0
    ans = 0
    A = []
    B = []

        # 행 비교
    for i in range(8):
        for j in range(8 -N +1):
            for a in range(N):
                A.append(word_table[i][j+a])
            B = A.copy()
            A.reverse()
            if A == B:
                cnt += 1
            A.clear()
            B.clear()

    # 열 비교
    for j in range(8):
        for i in range(8 -N +1):
            for a in range(N):
                A.append(word_table[i+a][j])
            B = A.copy()
            A.reverse()
            if A == B:
                cnt += 1
            A.clear()
            B.clear()
    print("#{} {}".format(t, cnt))