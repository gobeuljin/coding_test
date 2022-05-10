t = int(input())
for e in range(1, t+1):

    w  = list(map(str, input()))
    w = list(w)

    r = w.copy()

    for i in range(len(w)):
        r[i] = w[len(w)-1 -i]

    if r == w:
        print("#{0} 1".format(e))
    else:
        print("#{0} 0".format(e))
