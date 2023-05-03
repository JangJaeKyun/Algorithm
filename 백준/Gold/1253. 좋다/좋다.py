import sys
input = sys.stdin.readline

n = int(input())

num = list(map(int, input().split()))
num.sort()

count = 0

for i in range(n):
    start = 0
    end = n - 1
    while start < end:
        if i == start:
            start += 1
        elif i == end:
            end -= 1
        elif num[i] > num[start] + num[end]:
            start += 1
        elif num[i] < num[start] + num[end]:
            end -= 1
        elif num[i] == num[start] + num[end]:
            count += 1
            break

print(count)