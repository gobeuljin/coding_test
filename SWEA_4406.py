m = int(input())
for t in range(1, m+1):
    word = input()
    a = "aeiou"
    word = "".join(i for i in word if i not in a)

    print("#{} {}".format(t, word))