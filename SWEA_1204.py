m = int(input())
for t in range(1, m+1):
    tc = int(input())
    N_list = list(map(int, input().split()))

    N_list.sort()
    cnt = 0
    ans_cnt = 0
    ans_pos = 0
    for i in range(999):
        if N_list[i] == N_list[i+1]:
            cnt += 1
        else:
            if cnt >= ans_cnt: # >= 같아도 바꿔 줌으로서 동일 횟수 시에 더 큰값을 지정한다.
                ans_pos = N_list[i]
                ans_cnt = cnt
                cnt = 0
            else:
                cnt = 0

    print("#{0} {1}".format(tc, ans_pos))