import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(start, depth):
    # 현재 노드를 방문 처리
    visited[start] = True
    # 현재 노드와 연결된 다른 노드들에 대해서 재귀적으로 DFS 호출
    for i in graph[start]:
        if not visited[i]:
            dfs(i, depth + 1)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)] # 각 노드에 대한 인접 리스트
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b) # a와 b 사이에 간선 추가
    graph[b].append(a) # 양방향 그래프이므로 b와 a 사이에도 간선 추가

# 방문처리
visited = [False] * (n + 1)
count = 0 # 그래프 개수 저장

# 1 ~ n번 노드를 각각돌면서
for i in range(1, n + 1):
    if not visited[i]: # 만약 i번째 노드를 방문하지 않는다면
        if not graph[i]: # 만약 해당 정점이 연결된 그래프가 없다면
            count += 1 # count에 + 1
            visited[i] = True # 방문 처리
        else: # 연결된 그래프가 있다면
            dfs(i, 0) # dfs탐색
            count += 1 # 개수를 + 1

print(count)