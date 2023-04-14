a = int(input())
A = list(map(int, input().split()))
count = [1 for _ in range(a)]

for i in range(a):
    for j in range(i):
        if A[i] > A[j]:
            count[i] = max(count[i], count[j]+1)

print(max(count))