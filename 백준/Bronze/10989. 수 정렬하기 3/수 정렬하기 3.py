import sys
num = int(sys.stdin.readline())

count = [0] * 10001
for _ in range(num):
    a = int(sys.stdin.readline())
    count[a] += 1
    
for i in range(10001):
    while count[i] > 0:
        print(i)
        count[i] -= 1