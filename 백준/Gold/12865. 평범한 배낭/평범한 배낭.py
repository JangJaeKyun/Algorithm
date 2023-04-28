import sys
input = sys.stdin.readline

n, k = map(int, input().split())

# d[i][j] : i번째 물건까지 고려했을 때, 용량 j를 가지는 배낭에 담을 수 있는 물건들의 최대 가치
d = [[0] * (k + 1) for _ in range(n)]

weight = []
value = []
for _ in range(n):
    w, v = map(int, input().split())
    weight.append(w)
    value.append(v)

# 0/1 Knapsack 문제를 해결하는 DP 알고리즘
for i in range(n):
    for j in range(k + 1):
        # 현재 물건을 배낭에 넣을 수 있는 경우
        if j >= weight[i]:
            # 이전 물건(i-1)까지 선택한 경우와 현재 물건(i)을 선택한 경우 중, 최대 가치를 선택
            d[i][j] = max(d[i-1][j], d[i-1][j-weight[i]] + value[i])
        # 현재 물건을 배낭에 넣을 수 없는 경우, 이전 물건(i-1)까지 선택한 경우의 최대 가치와 동일
        else:
            d[i][j] = d[i-1][j]

# 물건을 전부 고려했을 때, 용량 k를 가지는 배낭에 담을 수 있는 물건들의 최대 가치 출력
print(d[n-1][k])