m = int(input())
for t in range(1, m+1):
    N_list=list(map(int, input().split()))
    N_list.sort()
    ans = 0
    for i in range(8):
        ans += N_list[i+1]

    print("#{0} {1}".format(t, int(round(ans/8, 0))))