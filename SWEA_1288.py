t = int(input())
for e in range(1, t+1):
    n = int(input())
    n_init = n
    n_list = list(str(n))
    n_list = list(map(int, n_list))
    n_s = set(n_list)
    m = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    N = 1
    while 1:
        if m - n_s == set():
            print("#{0} {1}".format(e, N*n_init))
            break
        else:
            N += 1
            n = n_init*N
            n = str(n)
            n_list = list(n)
            n_list = list(map(int, n_list))
            for i in n_list:
                n_s.add(i)
