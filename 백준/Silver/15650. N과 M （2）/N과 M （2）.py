import sys
input = sys.stdin.readline
from itertools import combinations

N, M = map(int, input().split())

num = []
for i in range(1, N+1):
    num.append(i)

for j in combinations(num, M):
    print(*j)