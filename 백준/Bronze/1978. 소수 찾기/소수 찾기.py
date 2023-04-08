count = int(input())

num = map(int, input().split())
sosu = []
for i in num:
    for j in range(2, i+1):
        if (j == i):
            sosu.append(i)
        elif (i % j == 0):
            break
print(len(sosu))