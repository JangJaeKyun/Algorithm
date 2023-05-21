n = int(input())

# dp[i]: i원을 거슬러주는 데 필요한 최소 동전 개수
dp = [float('inf')] * (n + 1)
dp[0] = 0

coins = [3, 5]

for coin in coins:
    for i in range(coin, n + 1):
        dp[i] = min(dp[i], dp[i - coin] + 1)

if dp[n] == float('inf'):
    print(-1)
else:
    print(dp[n])