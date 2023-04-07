t =int(input())

for i in range(t):
    OX = input()
    score = 0
    cnt = 0
    for j in range(len(OX)):
        if OX[j] == "O":
            cnt += 1
            score += cnt
        elif OX[j] == "X":
            score += 0
            cnt = 0
    print(score)