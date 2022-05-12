### 오답 ###

m = int(input())
for t in range(1, m+1):
    a = []
    
    ans = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(9):
        a.append(list(map(int, input().split())))
    s = 0

    for i in range(9):
        b = a[i].copy()
        b.sort()
        if b != ans:
            s += 1


    for i in range(9):
        b = []
        for j in range(9):
            b.append(a[i][j])
            b.sort()
        if b != ans:
            s += 1

    # p = 1
    # q = 0  
    # for e in range(1, 10):
    #     b = []
    #     for i in range(3):
    #         for j in range(3):
    #             b.append(a[i+q][j+((p-1)*3)])  
    #     b.sort()
    #     if b != ans:
    #         s += 1

    #     p += 1
    #     if e%3 == 0:
    #         q += 3
    #         p = 1
    
    b = []
    for i in range(3):
        for j in range(3):
            b.append(a[i][j])
    b.sort()
    if b != ans:
        s += 1

    b = []
    for i in range(3):
        for j in range(3, 6):
            b.append(a[i][j])
    b.sort()
    if b != ans:
        s += 1
    
    b = []
    for i in range(3):
        for j in range(6, 9):
            b.append(a[i][j])
    b.sort()
    if b != ans:
        s += 1

    b = []
    for i in range(3, 6):
        for j in range(3):
            b.append(a[i][j])
    b.sort()
    if b != ans:
        s += 1

    b = []
    for i in range(3, 6):
        for j in range(3, 6):
            b.append(a[i][j])
    b.sort()
    if b != ans:
        s += 1

    b = []
    for i in range(3, 6):
        for j in range(6, 9):
            b.append(a[i][j])
    b.sort()
    if b != ans:
        s += 1

    b = []
    for i in range(6, 9):
        for j in range(3):
            b.append(a[i][j])
    b.sort()
    if b != ans:
        s += 1

    b = []
    for i in range(6, 9):
        for j in range(3, 6):
            b.append(a[i][j])
    b.sort()
    if b != ans:
        s += 1

    b = []
    for i in range(6, 9):
        for j in range(6, 9):
            b.append(a[i][j])
    b.sort()
    if b != ans:
        s += 1

    
    if s == 0:
        print("#{0} {1}".format(t,1))
    else:
        print("#{0} {1}".format(t,0))
