for i in range(10):
    t = int(input())
    password = list(map(int, input().split()))

    cnt = 1
    cycle_cnt = 0
    while 1:

        if password[0] - cnt > 0 :
            password.append(password[0] - cnt)
            del password[0]
            cnt += 1
            cycle_cnt += 1
        
        else:
            password.append(0)
            del password[0]
            break

        if cycle_cnt == 5:
            cnt = 1
            cycle_cnt = 0

    print("#{} {} {} {} {} {} {} {} {}".format(t, password[0], password[1], password[2], password[3], password[4], password[5], password[6], password[7]))