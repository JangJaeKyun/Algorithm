import sys
input = sys.stdin.readline

def bfs(x,y):           
    queue = [(x,y)]
    visited[x][y] = 0 # 방문처리

    while queue:
        x,y = queue.pop(0)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue

            if visited[nx][ny] == 1 :
                queue.append((nx,ny))
                visited[nx][ny] = 0

T = int(input())

dx = [-1,1,0,0]
dy = [0,0,-1,1]
for _ in range(T):
    M, N, K = map(int, input().split())
    visited = [[0]*(N) for _ in range(M)]
    count = 0
    for _ in range(K):
        x,y = map(int, input().split())
        visited[x][y] = 1
    
    for i in range(M):
        for j in range(N):
            if visited[i][j] == 1:
                bfs(i,j)
                count += 1

    print(count)
   