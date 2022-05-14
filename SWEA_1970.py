m = int(input())
for t in range(1, m+1):
    N = int(input())
    cnt_50000 = 0
    cnt_10000 = 0
    cnt_5000 = 0
    cnt_1000 = 0
    cnt_500 = 0
    cnt_100 = 0
    cnt_50 = 0
    cnt_10 = 0

    while N >= 50000:
        N -= 50000
        cnt_50000 += 1

    while N >= 10000:
        N -= 10000
        cnt_10000 += 1

    while N >= 5000:
        N -= 5000
        cnt_5000 += 1

    while N >= 1000:
        N -= 1000
        cnt_1000 += 1

    while N >= 500:
        N -= 500
        cnt_500 += 1

    while N >= 100:
        N -= 100
        cnt_100 += 1

    while N >= 50:
        N -= 50
        cnt_50 += 1

    while N >= 10:
        N -= 10
        cnt_10 += 1
    print("#{}".format(t))
    print(cnt_50000, cnt_10000, cnt_5000, cnt_1000, cnt_500, cnt_100, cnt_50, cnt_10)