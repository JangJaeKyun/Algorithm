import sys
from math import lcm
Input = sys.stdin.readline

N = int(input())

for _ in range(N):
	a, b = map(int, input().split())
	print(lcm(a, b))