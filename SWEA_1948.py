m = int(input())
for t in range(1, m+1):
    m1, d1, m2, d2 = map(int, input().split())

    ans = 0
    last_day = [31,28,31,30,31,30,31,31,30,31,30,31]

    if m2 == m1:
        ans = d2 - d1 +1

    else: #달이 다를경우
        ans = (sum(last_day[m1-1:m2-1])) + (d2 - d1) +1

    print("#{0} {1}".format(t,ans))