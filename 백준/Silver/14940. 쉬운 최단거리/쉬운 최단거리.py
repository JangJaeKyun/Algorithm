import sys
from collections import deque
input = sys.stdin.readline

def bfs():

    queue = deque()


    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                queue.append((i, j))
                dist[i][j] = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if graph[nx][ny] == 0:
                continue

            if dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1 
                queue.append((nx, ny))

    return dist

n, m = map(int, input().split())

graph = []
for i in range(n):
    a = list(map(int, input().strip().split()))
    graph.append(a)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

dist = [[-1 if graph[i][j] != 0 else 0 for j in range(m)] for i in range(n)]

bfs()

for i in range(n):
    for j in range(m):
        print(dist[i][j], end=" ")
    print()