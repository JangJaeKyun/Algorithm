import sys
input = sys.stdin.readline

d1 = list(input().strip())
d2 = list(input().strip())
d3 = list(input().strip())
x, y, z = len(d1), len(d2), len(d3)

# LCS 길이를 저장하기 위한 이차원 리스트를 생성합니다.
# 행은 d2의 문자열을, 열은 d1의 문자열을 나타냅니다.
# 각 요소는 0으로 초기화됩니다.
chack = [[[0] * (z+1) for _ in range(y + 1)] for _ in range(x + 1)]
# d1과 d2의 각 문자를 비교하면서 LCS 길이를 구합니다.
for i in range(1, x + 1):
    for j in range(1, y + 1):
        for k in range(1, z + 1):
        # 현재 비교하는 문자가 같다면
            if d1[i - 1] == d2[j - 1] == d3[k - 1]:
                # 이전까지 구한 LCS 길이에 1을 더하여 저장합니다.
                chack[i][j][k] = chack[i - 1][j - 1][k - 1] + 1
            # 현재 비교하는 문자가 다르다면    
            else:
                # 현재 비교하는 문자가 다르다면
                chack[i][j][k] = max(chack[i][j][k - 1], chack[i][j - 1][k], chack[i - 1][j][k])

# 최종적으로, chack[x][y]에 저장된 값이 최장 공통 부분 수열의 길이가 됩니다.
print(chack[x][y][z])