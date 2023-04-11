n, r, c = map(int, input().split())

num = 0

while n > 1:
    ran = 2 ** (n - 1)
    if r >= ran:
        if c >= ran:
            num += (4 ** (n - 1)) * 3
            r -= ran
            c -= ran
        else:
            num += (4 ** (n - 1)) * 2
            r -= ran
            
    else:
        if c >= ran:
            num += (4 ** (n - 1)) * 1
            c -= ran
        else:
            pass
    
    n -= 1

if r == 0:
    if c == 0:
        print(num)
    else:
        print(num + 1)
else:
    if c == 0:
        print(num + 2)
    else:
        print(num + 3)