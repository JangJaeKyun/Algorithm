import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
connect = [[] for _ in range(n + 1)] # 연결 정보
needs = [[0] * (n + 1) for _ in range(n + 1)] # 각 제품을 만들때 필요한 부품
queue = deque() # 위상 정렬
degree = [0] * (n + 1) # 진입 차수
m = int(input())
for _ in range(m):
    a, b, c = map(int, input().split()) # x 부붐번호 y 필요한 부품 번호 k 필요한 개수
    connect[b].append((a, c)) # 필요부품 번호 인덱스에 만들 부품, 필요 숫자를 넣어줌
    degree[a] += 1 # 만들 부품 인덱스에 간선 정보 + 1

for i in range(1, n + 1):
    # 진입 차수가 0인걸 넣어준다.
    if degree[i] == 0: # i번째 진입 차수가 0이면
        queue.append(i) # 큐에 넣어준다

# 위상 정렬 시작
while queue: # 큐가 빌 때 까지
    now = queue.popleft()
    # 현 제품의 다음 단계 번호, 현 제품이 얼마나 필요한지
    for next, next_need in connect[now]:
        # 만약 현 제품이 기본 부품이면
        if needs[now].count(0) == n + 1:
            needs[next][now] += next_need
        # 현 제품이 중간 부품이면
        else: 
            for i in range(1, n + 1):
                needs[next][i] += needs[now][i] * next_need
        # 차수 - 1
        degree[next] -= 1
        if degree[next] == 0:
            # 차수 0이면 큐에 넣음
            queue.append(next)

for x in enumerate(needs[n]):
    if x[1] > 0:
        print(*x)