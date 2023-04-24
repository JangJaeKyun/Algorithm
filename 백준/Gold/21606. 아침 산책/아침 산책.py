import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def calPaths(graph: list, col: list) -> int:
    count = 0
    visited = set()

    def dfs(exterior: int) -> int:
        cnt = 0
        for neighbor in graph[exterior]:
            # 현재 방문 중인 노드가 실내 노드에 인접한 경우
            if col[neighbor] == 1:
                cnt += 1
            # 현재 방문 중인 노드가 실외 노드에 인접한 경우
            else:
                if neighbor not in visited:
                    visited.add(neighbor)
                    cnt += dfs(neighbor)
        return cnt

   # 각 노드를 방문하며, 실내 노드와 실외 노드 간의 경로 개수를 구합니다.
    for i in range(1, numVertices + 1):
        # 실내 노드와 인접한 실내 노드를 구하여 count 변수에 더합니다.
        if col[i] == 1:
            for j in graph[i]:
                if col[j] == 1:
                    count += 1
        # 방문하지 않은 노드를 시작점으로 dfs 함수를 호출합니다.
        # dfs 함수가 반환하는 값에 (n-1)을 곱한 값을 count 변수에 더합니다.
        else:
            if i not in visited:
                visited.add(i)
                tmp = dfs(i)
                count += tmp * (tmp - 1)
 
    return count

if __name__ == '__main__':
    # 노드 수(numVertices), 각 노드의 실내/실외 여부(col), 
    # 그리고 노드 간의 연결 관계를 나타내는 인접 리스트(graph)를 입력받습니다.
    
    numVertices = int(input())
    col = list(map(int, list("0"+input().strip())))

    graph = [[] for _ in range(numVertices + 1)]
    
    for _ in range(1, numVertices):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)

    # calPaths 함수를 호출하고, 반환된 경로 개수를 출력합니다.
    print(calPaths(graph, col))