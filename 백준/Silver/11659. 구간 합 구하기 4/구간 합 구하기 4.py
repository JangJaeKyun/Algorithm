import sys
input = sys.stdin.readline

n, m = map(int, input().split())

num = list(map(int, input().split()))
result = [0] * (n + 1)

k = 0
for i in range(n):
    k += num[i]
    result[i+1] = k

for j in range(m):
    a, b = map(int, input().split())
    anw = result[b] - result[a - 1]
    print(anw)