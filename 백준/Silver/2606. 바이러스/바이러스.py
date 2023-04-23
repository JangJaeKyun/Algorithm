import sys
input = sys.stdin.readline

# 깊이 우선 탐색 함수 dfs 정의
def dfs(graph, root):
    # 현재 노드 방문 처리
    visited[root] = True
    # 현재 노드와 연결된 다른 노드들에 대해서 재귀적으로 DFS 호출
    for i in graph[root]:
        if visited[i] == False:
            dfs(graph, i)

# 정점의 개수와 간선의 개수 입력 받기
n = int(input())
m = int(input())

# 각 노드에 대한 인접 리스트 만들기
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    # 양방향 그래프이므로 a와 b 사이에 간선 추가
    graph[a].append(b)
    graph[b].append(a)

# 방문 여부를 저장할 리스트 만들기
visited = [False] * (n + 1)

# 1번 정점을 시작으로 DFS 탐색 실행
dfs(graph, 1)

# 1번 정점을 제외한 방문한 정점의 개수 계산
ans = visited.count(True) - 1

# 결과 출력
print(ans)