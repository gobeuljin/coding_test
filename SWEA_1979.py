m = int(input())
for t in range(1, m+1):
    n, k = map(int, input().split())

    z = [list(map(int, input().split())) for _ in range(n)]

    cnt = 0
    sol = 0
    for i in range(n):
        for j in range(n):
            if z[i][j] == 1:
                cnt += 1
            if z[i][j] == 0 or j == n-1:
                if cnt == k:
                    sol += 1
                cnt = 0

    for j in range(n):
        for i in range(n):
            if z[i][j] == 1:
                cnt += 1
            if z[i][j] == 0 or i == n-1:
                if cnt == k:
                    sol += 1
                cnt = 0
    print("#{0} {1}".format(t, sol))