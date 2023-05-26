import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
anw = []
dp = [0] * n
count = 0
for i in range(n):
    anw.append((num[i], i))

anw.sort()

for j in range(1, n):
    if anw[j][0] != anw[j - 1][0]:
        count += 1
    dp[anw[j][1]] = count

print(*dp)