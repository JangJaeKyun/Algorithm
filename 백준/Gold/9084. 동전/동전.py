import sys
input = sys.stdin.readline


t = int(input())
for _ in range(t):
    # 각 테스트 케이스에서 동전의 종류 수, token, m을 입력받음
    n = int(input()) # 동전의 종류 수
    token = list(map(int, input().split())) # 동전의 종류와 금액
    m = int(input()) # 목표 금액

    # d 배열 초기화
    d = [0] * (m + 1)
    d[0] = 1

    # 모든 동전을 검사하면서 d 배열을 갱신함
    for coin in token:
        for i in range(m + 1):
            # 현재 검사 중인 동전의 금액보다 현재 인덱스(i)가 크거나 같은 경우에만 계산을 함
            if i >= coin:
                # d[i]는 d[i-coin]으로 갱신함. 이는 현재 동전을 사용하지 않는 경우와 현재 동전을 사용하는 경우를 고려한 것임
                d[i] += d[i - coin]
    
    # 주어진 동전으로 만들 수 있는 금액 중 목표 금액을 만들 수 있는 경우의 수를 출력함
    print(d[m])