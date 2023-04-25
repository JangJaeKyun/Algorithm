import sys
from collections import deque
input = sys.stdin.readline
import heapq

def bfs(a, b):
    # 큐(queue) 구현을 위해 deque 라이브러리 사용
    global count
    queue = []
    heapq.heappush(queue,(count, a, b))
    # 큐가 빌 때까지 반복
    while queue:
        count, x, y = heapq.heappop(queue)
        if x == (n-1) and y == (n-1):
            return
        # if visited[x][y]:
        #     continue
        # 현제 방향에서 4가지 방향으로 위치 확인
        for i in range(4): 
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            # 벽인 경우 무시
            if graph[nx][ny] == 0 and not visited[nx][ny]:
                new_count = count + 1
                visited[nx][ny] = True
                heapq.heappush(queue, (new_count, nx, ny))
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                heapq.heappush(queue, (count, nx, ny))
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return

# n, m을 공백을 기준으로 구분하여 입력 받기
n = int(input())
# 2차원 리스트의 맵 정보 입렵 받기
graph = []
for i in range(n):
    a = list(map(int, input().strip()))
    graph.append(a)

visited = [[False] * (n + 1) for _ in range(n + 1)]

# 이동할 네 가지 방향 정의(상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

count = 0
bfs(0, 0)
print(count)