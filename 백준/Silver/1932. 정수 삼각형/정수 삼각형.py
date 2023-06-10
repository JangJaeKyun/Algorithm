import sys
input = sys.stdin.readline

N = int(input())

nums = []
for _ in range(N):
    nums.append(list(map(int, input().split())))

for i in range(1,N):
  for j in range(len(nums[i])):
    if j == 0:
      nums[i][j] = nums[i][j] + nums[i - 1][j]
    elif j == len(nums[i]) - 1: 
      nums[i][j] = nums[i][j] + nums[i - 1][j - 1]
    else:
      nums[i][j]=max(nums[i - 1][j - 1],nums[i - 1][j])+nums[i][j]
print(max(nums[N - 1]))