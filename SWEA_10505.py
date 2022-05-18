m = int(input())
for t in range(1, m+1):
    N = int(input())
    a = list(map(int, input().split()))
    avg = sum(a) / len(a)
    cnt =0
    for i in range(len(a)):
        if avg >= a[i]:
            cnt += 1

    print("#{} {}".format(t, cnt))

