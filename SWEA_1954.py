m = int(input())
for t in range(1, m+1):
    n = int(input())
    a = [i for i in range(1, n*n +1)]
    b = [[0 for i in range(n)] for i in range(n)]

    cnt = 1
    x = 0
    y = 0

    while cnt != 2*n:
        
        if cnt % 4 == 1:
            for i in range(n-x):
                b[0 + (x//2)][i + (x//2)] = a[y]
                y += 1
            cnt += 1
            x += 1

        elif cnt %2 == 0 and cnt %4 != 0:
            for i in range(n-x):
                b[i+(cnt//4 +1)][n-(cnt//4 +1)] = a[y]
                y += 1
            cnt += 1

        elif cnt %4 == 3:
            for i in range(n-x):
                b[n-(cnt//4 +1)][n-(cnt//4 +1) - (i+1)] = a[y] #b[n-(cnt//4 +1)][n-(cnt//4 +1) - (i+(cnt//4 +1))]
                y += 1
            cnt+= 1
            x += 1

        else:
            for i in range(n-x):
                b[(n-1- (cnt//4)) - i][(cnt//4) - 1] = a[y]
                y += 1
            cnt += 1
    print("#{}".format(t))
    for i in range(n):
        for j in range(n):
            print(b[i][j], end=" ")
        print("")