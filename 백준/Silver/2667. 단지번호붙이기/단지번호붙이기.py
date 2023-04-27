import sys
input = sys.stdin.readline

def dfs(x,y): 
    if x <= -1 or x >= n or y <= -1 or y >= n :
        return 0
    if graph[x][y] == 0:
        return 0
    graph[x][y] = 0
    count = 1
    count += dfs(x - 1, y)
    count += dfs(x, y - 1)
    count += dfs(x + 1, y)
    count += dfs(x, y + 1)
    return count

n = int(input())
 
graph = []
for i in range(n):
    graph.append(list(map(int,input().strip())))

counts = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            count = dfs(i, j)
            counts.append(count)

counts.sort()
print(len(counts))
for count in counts:
    print(count)