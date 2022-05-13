m = int(input())
for t in range(1, m+1):
    n = int(input())
    a = [1, 1]
    pre_a = [1, 1]
    print("#{}".format(t))
    if n == 1:
        a = [1]
        print(1)

    elif n == 2:
        a =[1,1]
        print(1)
        print(1, 1)

    else: # n이 3이상
        print(1)
        print(1, 1)
        for i in range(1, n-1):
            a.insert(1, 5)
            for j in range(1, i+1):
                a[j] = pre_a[j-1] + pre_a[j]
            pre_a = a.copy()
            print(*a)
