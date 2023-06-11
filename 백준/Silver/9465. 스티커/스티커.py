import sys
input = sys.stdin.readline

T = int(input())

nums = []
for _ in range(T):
    n = int(input())
    nums = []
    for _ in range(2):
        nums.append(list(map(int, input().split())))
    for j in range(1, n):
        if j == 1:
            nums[0][j] += nums[1][j - 1]
            nums[1][j] += nums[0][j - 1]
        else:
            nums[0][j] += max(nums[1][j - 1], nums[1][j - 2])
            nums[1][j] += max(nums[0][j - 1], nums[0][j - 2])
    print(max(nums[0][n - 1], nums[1][n - 1]))