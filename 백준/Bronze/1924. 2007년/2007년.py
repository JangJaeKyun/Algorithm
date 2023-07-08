x, y = map(int, input().split())

big_month = [1, 3, 5, 7, 8, 10, 12]
normal_month = [4, 6, 9, 11]
small_month = [2]

day = 0
for i in range(1, x):
    if i in big_month:
        day += 31
    elif i in normal_month:
        day += 30
    elif i in small_month:
        day += 28

day += y

if day % 7 == 1:
    print("MON")
elif day % 7 == 2:
    print("TUE")
elif day % 7 == 3:
    print("WED")
elif day % 7 == 4:
    print("THU")
elif day % 7 == 5:
    print("FRI")
elif day % 7 == 6:
    print("SAT")
elif day % 7 == 0:
    print("SUN")