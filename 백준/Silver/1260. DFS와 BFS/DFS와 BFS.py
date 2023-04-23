import sys
import heapq
import itertools
from collections import deque
from queue import PriorityQueue
input = sys.stdin.readline

# DFS 함수 정의
def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    # 현재 노드 번호 출력
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드들에 대해서 재귀적으로 DFS 호출
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# BFS 함수 정의
def bfs(graph, v, visited):
    # BFS를 위한 큐 생성
    queue = deque([v])
    # 현재 노드를 방문 처리
    visited[v] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아서 출력
        v = queue.popleft()
        print(v, end=' ')
        # 아직 방문하지 않은 인접한 노드들에 대해서 방문 처리 후 큐에 추가
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 노드의 개수, 간선의 개수, 시작 노드 번호 입력
n, m, v = map(int, input().split())

# 노드들의 방문 여부를 저장하는 리스트 초기화
visited1 = [False] * (n + 1) # DFS를 위한 방문 여부 리스트
visited2 = [False] * (n + 1) # BFS를 위한 방문 여부 리스트

# 그래프 초기화
graph = [[] for _ in range(n+1)] # 각 노드에 대한 인접 리스트
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b) # a와 b 사이에 간선 추가
    graph[b].append(a) # 양방향 그래프이므로 b와 a 사이에도 간선 추가

# 노드 번호가 작은 순서대로 각 노드에 연결된 간선을 정렬
for i in range(1, n+1):
    graph[i].sort()

# DFS, BFS 호출
dfs(graph, v, visited1)
print()
bfs(graph, v, visited2)
print()