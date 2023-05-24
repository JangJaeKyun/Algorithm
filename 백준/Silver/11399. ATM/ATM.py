import sys
input = sys.stdin.readline

N = int(input())

num = list(map(int, input().split()))
num.sort()

dp = [0] * (N + 1)
dp[1] = num[0]
for i in range(2, N + 1):
    dp[i] = (dp[i - 1] + num[i - 1])

print(sum(dp))