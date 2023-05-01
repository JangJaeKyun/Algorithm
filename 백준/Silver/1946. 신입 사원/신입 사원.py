import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    count = 1
    rank = []
    for _ in range(N):
        grade = list(map(int, input().split()))
        rank.append(grade)
    rank.sort(key = lambda x:x[0])
    temp = rank[0]
    for i in range(1, N):
        if temp[1] > rank[i][1]:
            count += 1
            temp = rank[i]


    print(count)