def sumnum(n):
    if n == 1 :
        return 1
    elif n == 2 :
        return 2
    elif n == 3 :
        return 4
    else:
        return sumnum(n - 1) + sumnum(n - 2) + sumnum(n - 3)
    
t = int(input())

for _ in range(t):
    n = int(input())
    print(sumnum(n))