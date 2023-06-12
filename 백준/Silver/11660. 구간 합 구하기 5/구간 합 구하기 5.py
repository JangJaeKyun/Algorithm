import sys
input = sys.stdin.readline

n, m = map(int, input().split())
result = [[0] * (n + 1) for _ in range(n + 1)]

k = 0
for i in range(1, n + 1):
    nums = list(map(int, input().split()))
    k = 0
    for j in range(1, n + 1):
        k += nums[j-1]
        result[i][j] = k + result[i-1][j]
        
for j in range(m):
    a, b, c, d = map(int, input().split())
    ans = result[c][d] - result[a-1][d] - result[c][b-1] + result[a-1][b-1]
    print(ans)