import sys
input = sys.stdin.readline

N, K = map(int, input().split())

money = []
count = 0

for _ in range(N):
    A = int(input())
    money.append(A)
    # 리스트를 내림차순으로 바꿈
    money.sort(reverse=True)

for coin in money:
    # 목표금액에서 뺄 수 있는 큰 수 부터 빼기
    # count에는 K원을 만드는데 필요한 동전 개수
    count += K // coin 
    K %= coin

print(count)