import sys
input = sys.stdin.readline
from collections import Counter

N = int(input())

for i in range(N):
    M = int(input())
    ans = []
    for j in range(M):
        A, B = input().split()
        ans.append(B)

    clothes_Counter = Counter(ans)
    count = 1
    
    for z in clothes_Counter:
        count *= clothes_Counter[z] + 1

    print(count - 1)
