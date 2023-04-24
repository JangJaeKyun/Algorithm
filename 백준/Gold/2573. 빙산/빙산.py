import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def dfs(i, j):#2가지 경우로 나뉘는걸 체크해주기 위한 함수.
    for k in range(4): # 상하좌우 4방향에 대해 탐색
        nx = dx[k] + i # 새로운 좌표 탐색
        ny = dy[k]+j
        if 0 <= nx < n and 0 <= ny < m and vist[nx][ny]: # 새로운 좌표가 범위 안에 있고 방문하지 않은 좌표라면
            vist[nx][ny] = False # 방문 표시
            if s[nx][ny] != 0: # 새로운 좌표가 0이 아니라면
                dfs(nx,ny) # 새로운 좌표로 dfs 재귀 호출
            

input = sys.stdin.readline
n,m = map(int,input().split())
s=[list(map(int,input().split())) for _ in range(n)]
dx = [1, -1, 0, 0] #상하좌우 이동
dy = [0, 0, 1, -1]
vist = [[False] * m for _ in range(n)] # 방문 체크
t = 0

while True:
    t += 1 # 연도 + 1
    for i in range(n):
        for j in range(m):
            if s[i][j] != 0: # 빙산 위치
                vist[i][j] = True # 방문 표시
                c = s[i][j] # 빙산 높이 저장
                for k in range(4): # 상하좌우 네 방향 반복문
                    nx = dx[k] + i # 상하좌우 힌 칸 이동한 새로운 위치를 계산
                    ny = dy[k] + j
                    if 0 <= nx < n and 0 <= ny < m and not vist[nx][ny]: # 새로운 위치가 범위 안에 있고, 방문하지 않은 곳이라면
                        if s[nx][ny] == 0: # 새로운 위치가 바다면
                            c -= 1 # 빙산 높이 - 1
                            if c == 0: # 빙산 높이가 0이 되면 탐색 종료
                                break
                s[i][j] = c # 감소된 빙산 높이 저장
                
    count=0#영역의 개수
    for i in range(n):
        for j in range(m):
            if s[i][j] != 0 and vist[i][j]: # 해당 칸이 얼음이고 방문하지 않았으면
                dfs(i,j) # 현제 위치에서 dfs함수 호출
                count += 1 # count에 1을 더함
            elif s[i][j] == 0 and vist[i][j]: # 해당 칸이 바다이고 방문하지 않았으면
                vist[i][j] = False # 방문 처리
                
    if count >= 2:#영역이 2개 이상으로 나뉜경우니 출력해주고 반복문을 탈출한다.
        print(t) # 연도를 출력
        break
    elif count == 0:#한번에 녹았다는 의미이므로 0을 출력해주고 반복문을 탈출한다.
        print(0)
        break