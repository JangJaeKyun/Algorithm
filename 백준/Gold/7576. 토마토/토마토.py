import sys
import heapq
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

queue = deque()  # 큐 초기화

visited = [[False] * N for _ in range(M)]  # 방문 여부를 저장하는 2차원 리스트 초기화
dx = [-1, 1, 0, 0]  # 상하좌우 이동 방향을 나타내는 리스트
dy = [0, 0, -1, 1]
day = 0
graph = []  # 토마토의 상태를 저장하는 2차원 리스트 초기화

for _ in range(M):
    row = list(map(int, input().split()))
    graph.append(row)

for i in range(M):
    for j in range(N):
        if graph[i][j] == 1:  # 익은 토마토라면
            queue.append((i, j))  # 큐에 추가하여 BFS 시작점으로 설정
            visited[i][j] = True  # 해당 좌표를 방문했음을 표시

def bfs():
    while queue:
        x, y = queue.popleft()  # 큐에서 좌표를 꺼냄

        for i in range(4):  # 상하좌우로 이동
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue  # 범위를 벗어나면 무시

            if graph[nx][ny] == 0 and not visited[nx][ny]:  # 익지 않은 토마토이고 아직 방문하지 않았다면
                queue.append((nx, ny))  # 큐에 추가하여 다음에 방문할 좌표로 설정
                visited[nx][ny] = True  # 해당 좌표를 방문했음을 표시
                graph[nx][ny] = graph[x][y] + 1  # 익은 토마토로 표시하고, 날짜를 1일 증가시킴

bfs()  # BFS 수행

max_day = 0
for a in graph:
    for b in a:
        if b == 0:  # 아직 익지 않은 토마토가 있다면
            print(-1)  # -1 출력하고 프로그램 종료
            exit(0)
        max_day = max(max_day, b)

print(max_day - 1)