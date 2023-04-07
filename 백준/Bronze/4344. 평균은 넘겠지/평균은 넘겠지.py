c = int(input())

for _ in range(c):
    person = list(map(int, input().split()))
    result = sum(person[1:])
    average = result/person[0]
    count = 0
    for i in range(1, person[0]+1):
        if person[i] > average:
            count += 1
    a=round(count/person[0]*100, 3)

    print("{:.3f}%".format(a))