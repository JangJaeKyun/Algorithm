import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            nums.append([i, v])
            dfs(graph, i, visited)

n = int(input())
nums = []
graph = [[] for _ in range(n+1)] # 각 노드에 대한 인접 리스트
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b) # a와 b 사이에 간선 추가
    graph[b].append(a) # 양방향 그래프이므로 b와 a 사이에도 간선 추가

# 방문처리
visited = [False] * (n+1)

dfs(graph, 1, visited)

nums.sort()
for i in range(n - 1):
    print(nums[i][1])
