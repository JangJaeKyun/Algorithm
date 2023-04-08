num = int(input())

hanso = 0
for i in range(1, num+1):
    hanso_list = list(map(int, str(i)))
    if i < 100:
        hanso += 1
    elif hanso_list[0]-hanso_list[1] == hanso_list[1]-hanso_list[2]:
        hanso += 1
print(hanso)