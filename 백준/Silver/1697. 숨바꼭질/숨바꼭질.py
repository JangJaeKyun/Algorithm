import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

def bfs(v):
    queue = deque([v])
    while queue:
        v = queue.popleft()
        if v == k:
            return array[v]
        for next_v in (v-1, v+1, 2*v):
            if 0 <= next_v < MAX and not array[next_v]:
                array[next_v] = array[v] + 1
                queue.append(next_v)

MAX = 100001
array = [0] * MAX
print(bfs(n))