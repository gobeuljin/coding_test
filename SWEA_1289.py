m = int(input())
for t in range(1, m+1):
    a = input()
    a = list(a)
    initial_zero = ["0" for i in range(len(a))]
    change_pos = 0
    cnt = 0

    change_pos = a.index("1") # 앞에 0들을 지우기 위한 초기작업
    del a[:change_pos]
    del initial_zero[:change_pos]

    while  1: 
  
        change_pos = 0
        cnt += 1
        for i in range(change_pos, len(a)):
            initial_zero[i] =initial_zero[i].replace("0", "1")
        
        if initial_zero == a:
            break
        else:
            change_pos = a.index("0")
            del a[:change_pos]
            del initial_zero[:change_pos]

        cnt += 1
        for i in range(len(a)):
            initial_zero[i] =initial_zero[i].replace("1", "0")
        
        if initial_zero == a:
            break
        else:
            change_pos = a.index("1")
            del a[:change_pos]
            del initial_zero[:change_pos]

    print("#{} {}".format(t, cnt))