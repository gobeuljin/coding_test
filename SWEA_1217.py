def ee(a, b):
    c = 1
    if b <= 0:
        return 1
    else:
        while b != 0:
            c = c*a
            b -= 1
    return c

for i in range(10):
    t = int(input())
    a, b = map(int, input().split())
    
    print("#{} {}".format(t, ee(a,b)))
    
