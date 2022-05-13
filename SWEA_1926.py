N  = int(input())
game = [str(i) for i in range(1, N+1)]
cnt = 0
for i in range(N):
    if "3" in game[i] or "6" in game[i] or "9" in game[i]:
        for j in range(len(game[i])):
            if game[i][j] == "3" or game[i][j] == "6" or game[i][j] == "9":
                cnt += 1
        print("-"*cnt, end=" ")
        cnt = 0


    else:
        print(game[i], end=" ")
