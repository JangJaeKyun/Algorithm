def prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

t = int(input())
for _ in range(t):
    num = int(input())
    num1 = num // 2
    num2 = num // 2
    while True:
        if num1 == 0:
            break
        if prime(num1) and prime(num2):
            print(num1, num2)
            break
        else:
            num1 -= 1
            num2 += 1