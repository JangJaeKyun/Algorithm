import sys
input = sys.stdin.readline

n = int(input())
a = 2
b = 3
if n <= 3:
    print(n)
else:
    for i in range(4, n + 1):
        num = b + a
        a = b
        b = num % 15746

    print(b)