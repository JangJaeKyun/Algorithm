import sys
input = sys.stdin.readline
from itertools import permutations

N, M = map(int, input().split())

num = list(map(int, input().split()))

ans = []
for j in permutations(num, M):
    ans.append(j)

num = list(set(ans))
num.sort()
for i in range(len(num)):
    print(*num[i])