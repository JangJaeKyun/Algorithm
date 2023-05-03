import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

num = list(map(int, input().split()))
num.sort()

end = n - 1
start = 0
sum = 0
cnt = 0

while start < end:
    if m > num[start] + num[end]:
        start += 1
    elif m < num[start] + num[end]:
        end -= 1
    elif m == num[start] + num[end]:
        cnt += 1
        start += 1

print(cnt)