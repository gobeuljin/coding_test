a = int(input())
for t in range(1, a+1):
    h1 , m1 , h2, m2 = map(int, input().split())
    m = m1 + m2
    h = h1 + h2
    if m >= 60:
        m -= 60
        h += 1
    if 24>=h > 12:
        h -= 12
    elif h > 24:
        h -= 24

    print("#{} {} {}".format(t, h, m))