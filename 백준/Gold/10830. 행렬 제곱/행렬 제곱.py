import sys
import heapq
from collections import deque

n, b = map(int, input().split()) # n, b = 2, 5
c = []
for _ in range(n):
    c.append(list(map(int, sys.stdin.readline().split())))
# 행렬 곱셈 함수
def mul(a, b):
    result = [[0 for _ in range(n)] for _ in range(n)]  # 결과 행렬 초기화
    for i in range(n):  # 행
        for j in range(n):  # 열
            for k in range(n):  # 행과 열의 교차 지점
                result[i][j] += a[i][k] * b[k][j]  # 행렬 곱셈 수행
            result[i][j] %= 1000  # 1000으로 나눈 나머지 저장
    return result
# 분할정복 함수
def devide(b, c):
    if b == 1:  # b가 1일 경우 자기 자신 반환
        return c
    elif b == 2:  # b가 2일 경우 행렬 곱셈 수행
        return mul(c, c)
    else:  # b가 2보다 큰 경우 분할 정복 수행
        tmp = devide(b // 2, c)
        if b % 2 == 0:  # b가 짝수인 경우
            return mul(tmp, tmp)
        # b가 홀수일 경우 마지막에 A를 곱해줘야한다.
        # AAAAA = ((A^2)^2)*A
        else:
            return mul(mul(tmp, tmp), c)
        
result = devide(b, c)
for row in result:
    for num in row:
        print(num % 1000,end= ' ')
    print()