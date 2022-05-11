m = int(input())
for t in range(1, m+1):
    n = int(input())
    N = [list(map(int, input().split())) for i in range(n)]


    N_90 =[[0 for i in range(n)] for j in range(n)]
    N_180 =[[0 for i in range(n)] for j in range(n)]
    N_270 =[[0 for i in range(n)] for j in range(n)]

    #(i,j)
    for i in range(n): 
        for j in range(n): 
            N_90[i][j] = N[(n-1)-j][i] 

    for i in range(n): 
        for j in range(n): 
            N_180[i][j] = N_90[(n-1)-j][i] 

    for i in range(n): 
        for j in range(n): 
            N_270[i][j] = N_180[(n-1)-j][i] 
    print("#{}".format(t))
    for i in range(n):
        for j in range(n):
            print(str(N_90[i][j]), end="")
            if j == n-1:
                print(" ", end="")
        for k in range(n):
            print(str(N_180[i][k]), end="")
            if k == n-1:
                print(" ", end="")
        for l in range(n):
            print(str(N_270[i][l]), end="")
        print("")


