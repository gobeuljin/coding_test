t = int(input())
for p in range(1, t+1):
    ww = input()
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    max_1 = 0
    max_2 = 0
    if len(a) < len(b) :
        for k in range(len(a)):
            max_1 += a[k]*b[k]
        for i in range(len(b) - len(a) + 1):
            max_2 = 0
            for e in range(len(a)):
                max_2 += a[e]*b[e + i]
            if max_2 > max_1:
                max_1 = max_2
    else:
        for k in range(len(b)):
            max_1 += a[k]*b[k]
        for i in range(len(a) - len(b) + 1):
            max_2 = 0
            for e in range(len(b)):
                max_2 += b[e]*a[e + i]
            if max_2 > max_1:
                max_1 = max_2

    print("#{0} {1}".format(p, max_1))