import heapq
import sys
input = sys.stdin.readline

v,e = map(int,input().split())
start = int(input())-1
dist = [float('inf') for i in range(v)]
dist[start] = 0

linked = [[] for i in range(v)]
for i in range(e):
    a,b,w = map(int,input().split())
    linked[a-1].append((w,a-1,b-1))

heap = []
for w,a,b in linked[start]:
    heapq.heappush(heap, (0,w,a,b))
    
while(heap):
    d,w,a,b = heapq.heappop(heap)
    if dist[a]+w < dist[b]:
        dist[b] = dist[a]+w
        for w,x,y in linked[b]:
            heapq.heappush(heap,(dist[b],w,x,y))
            
for i in dist:
    print(i if i != float('inf') else "INF")