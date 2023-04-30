import sys
input = sys.stdin.readline

N, M = map(int, input().split())
small = [int(input()) for _ in range(M)]

# 이동할 수 있는 최대 속력 구하기
max_speed = int((2*N)**(1/2)) + 1

# DP 테이블 초기화
dp = [[float('inf')] * (max_speed+1) for _ in range(N+1)]

# 2번 돌다리가 없는 경우
if 2 not in small:
# 2번 돌다리에서의 이동 최소 횟수 초기화
    dp[2][1] = 1
    # 3번 돌다리부터 N번 돌다리까지
    for num in range(3, N+1):
    # num번 돌다리가 없는 경우
        if num not in small:
        # 현재 속력(이동거리)에 따른 최소 이동 횟수 계산
            for speed in range(1, max_speed):
                dp[num][speed] = min(dp[num - speed][speed - 1], dp[num - speed][speed], dp[num - speed][speed + 1]) + 1

# N번 돌다리까지의 최소 이동 횟수 계산
ans = min(dp[N])

# 도달할 수 없는 경우 -1 출력, 그 외에는 최소 이동 횟수 출력
if ans == float('inf'):
    print(-1)
else :
    print(ans)