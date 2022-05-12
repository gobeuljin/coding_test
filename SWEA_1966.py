m = int(input())
for t in range(1, m+1):
    n = map(int, input())
    a = map(int, input().split())
    a = list(map(int, a))
    a.sort()
    print("#{}".format(t), end=" ")
    for i in range(len(a)):
        print(a[i], end="")
        if i == len(a) -1:
            print("")
            break
        print(" ",end="")