m = int(input())
for t in range(1, m+1):
    N = int(input())
    ans = []

    #문자열 받아서 합치기
    for i in range(N):
        word, num = map(str, input().split())
        num = int(num)
        ans.append(word*num)
    ans = "".join(ans)

    ten_n = len(ans)//10 # 10 문자열씩 몇 번 자를것인지 

    print("#{}".format(t))
    for i in range(ten_n +1):
        print(ans[0+(10*i):10*(1+i)])
