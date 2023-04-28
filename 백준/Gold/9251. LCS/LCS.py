import sys
input = sys.stdin.readline

d1 = list(input().strip())
d2 = list(input().strip())
x, y = len(d1), len(d2)

chack = [[0] * (y+1) for _ in range(x+1)]

for i in range(1, x + 1):
    for j in range(1, y + 1):
        if d1[i - 1] == d2[j - 1]:
            chack[i][j] = chack[i - 1][j - 1] + 1
        else:
            chack[i][j] = max(chack[i][j-1], chack[i-1][j])
    
print(chack[x][y])