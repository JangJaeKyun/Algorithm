import sys
input = sys.stdin.readline

n = int(input())

count = 0
while n >= 0:
    if n % 5 != 0:
        n -= 3
        count += 1
    elif n % 5 == 0:
        count += n // 5
        print(count)
        break
else:
    print(-1)