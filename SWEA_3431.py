m = int(input())
for t in range(1, m+1):
    L, U, X = map(int, input().split())

    if X > U:
        print("#{0} {1}".format(t, -1))
    elif L <= X <= U:
        print("#{0} {1}".format(t, 0))
    else:
        print("#{0} {1}".format(t, L-X))