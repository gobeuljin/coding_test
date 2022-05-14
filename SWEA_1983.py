m = int(input())
for t in range(1, m+1):
    N, K = map(int, input().split())
    grade_table = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D"]
    #점수 입력
    grade = [list(map(int, input().split())) for i in range(N)]

    #점수 환산
    for i in range(N):
        grade[i][0] *= 0.35
        grade[i][1] *= 0.45
        grade[i][2] *= 0.2
        grade[i] = sum(grade[i])

    t_grade = grade.copy()

    # 점수 내림차순 정렬
    t_grade.sort(reverse=True)

    # K번호 점수가 몇번쨰인지 찾음
    for i in range(N):
        if grade[K-1] == t_grade[i]:
            pos = i
            break

    print("#{} {}".format(t,grade_table[pos // (N//10)]))