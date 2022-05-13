m = int(input())
for t in range(1, m+1):
    N , M = map(int, input().split())
    N_t = [list(map(int, input().split())) for _ in range(N)]

    #(N - M +1)^2 만큼 반복
    standard = N_t[1][1] + N_t[2][1] + N_t[1][2] + N_t[2][2]
    for i in range(N - M +1): # N - M +1 = 4 
        for j in range(N - M +1):
            a = b = 0
            M_t = 0
            for a in range(M):
                for b in range(M):
                    M_t += N_t[i+a][j+b]

            if M_t > standard:
                standard = M_t

    print("#{} {}".format(t, standard))