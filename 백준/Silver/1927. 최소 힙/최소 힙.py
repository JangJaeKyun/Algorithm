import sys
input = sys.stdin.readline
import heapq

N = int(input())

queue = []
for _ in range(N):
    x = int(input())
    if x != 0:
        heapq.heappush(queue, x)
    else:
        try:
            print(heapq.heappop(queue))
        except:
            print(0)