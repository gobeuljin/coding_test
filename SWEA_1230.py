for t in range(1, 11):
    pw_n = int(input())
    pw = list(map(int, input().split()))
    com_n = int(input())
    com = list(map(str, input().split()))
    com.append("U")
    while 1:
        x = 0
        y = 0
        s = 0
        if com[0] == "I":
            x = int(com[1])
            y = int(com[2])
            for i in range(y, 0, -1):
                pw.insert(x, int(com[2+i]))
            del com[:3+y] # I + x + y + y숫자
        
        elif com[0] == "D":
            x = int(com[1])
            y = int(com[2])
            del pw[x:x+y]
            del com[:3] # D + x + y
        
        elif com[0] == "A":
            y = int(com[1])
            for i in range(y):
                pw.append(int(com[2+i]))
            del com [:2+y] # A + y + y숫자
        else:
            break

    print("#{}".format(t), *pw[:10])