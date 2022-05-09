# 사용량 : W
# A 요금
# W x P 원
# B요금
# Q + (W - R) x S 원

t = int(input())

for i in range(1, t+1):
    P, Q, R, S, W = map(int, input().split())
    A = W*P
    if W > R :
        B = Q + (W - R) * S
    else:
        B = Q

    if A > B:
        print("#{0} {1}".format(i, B))
    else:
        print("#{0} {1}".format(i, A))