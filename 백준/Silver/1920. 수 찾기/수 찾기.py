N = int(input())
A = list(map(int, input().split()))
M = int(input())
arr = list(map(int, input().split()))
A.sort()


for num in arr:
    lt, rt = 0, N - 1
    isExit = False

    while lt <= rt:
        mid = (lt + rt) // 2
        if num == A[mid]:
            isExit = True
            print(1)
            break
        elif num > A[mid]:
            lt = mid + 1
        else:
            rt = mid - 1

    if not isExit:
        print(0)