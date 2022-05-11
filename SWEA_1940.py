m = int(input())
for t in range(1, m+1):
    n = int(input())
    distance = 0
    v = 0
    for i in range(n):
        com = []
        com = list(map(int,input().split()))
        if com[0] == 0:
            v += 0
        elif com[0] == 1:
            v += com[1]
        else:
            v -= com[1]
            if v < 0:
                v = 0
        
        distance += v

    print("#{0} {1}".format(t,distance))
