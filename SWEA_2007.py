m = int(input())
for t in range(1, m+1):
    word = input()
    word = list(word)
    if word[0:2] == word[2:4]:
        print("#{0} {1}".format(t, 2))
    elif word[0:3] == word[3:6]:
        print(("#{0} {1}".format(t, 3)))
    elif word[0:4] == word[4:8]:
        print(("#{0} {1}".format(t, 4)))
    elif word[0:5] == word[5:10]:
        print(("#{0} {1}".format(t, 5)))
    elif word[0:6] == word[6:12]:
        print(("#{0} {1}".format(t, 6)))
    elif word[0:7] == word[7:14]:
        print("#{0} {1}".format(t, 7))
    elif word[0:8] == word[8:16]:
        print(("#{0} {1}".format(t, 8)))
    elif word[0:9] == word[9:18]:
        print(("#{0} {1}".format(t, 9)))
    elif word[0:10] == word[10:20]:
        print(("#{0} {1}".format(t, 10)))



