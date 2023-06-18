import sys
input = sys.stdin.readline
from itertools import permutations

N, M = map(int, input().split())

num = list(map(int, input().split()))
num.sort()

for j in permutations(num, M):
    print(*j)