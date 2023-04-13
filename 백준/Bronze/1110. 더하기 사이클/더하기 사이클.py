t = int(input())
n = t

count = 0
while True:
    a = n % 100 // 10
    b = n % 10
    c = (a + b) % 10
    n = (b * 10) + c
    
    count += 1
    if n == t:
        break

print(count)