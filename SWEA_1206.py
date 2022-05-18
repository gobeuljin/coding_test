for t in range(1, 11):
    road_width = int(input())
    building = list(map(int, input().split()))
    spare = []
    cnt = 0
    for i in range(2, road_width-2):
        if building[i] > building[i-1] and building[i] > building[i-2] : # 왼쪽 조망이 확보가 되면
            if building[i] > building[i+1] and building[i] > building[i+2]: #오른쪽 조망
                spare.append(building[i-1])
                spare.append(building[i-2])
                spare.append(building[i+1])
                spare.append(building[i+2])
                spare.sort()
                cnt += building[i] - spare[3]
                spare.clear()
    print("#{} {}".format(t, cnt))