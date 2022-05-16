m = int(input())
for t in range(1, m+1):
    A, B = map(int, input().split())
    C = A + B
    if C >= 24:
        C -= 24

    print("#{} {}".format(t, C))