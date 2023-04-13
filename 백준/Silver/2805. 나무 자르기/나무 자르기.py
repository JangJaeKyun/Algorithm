import sys

n, m = map(int, input().split())
tree = list(map(int, input().split()))
start, end = 1, max(tree) # 이분탐색 범위

while start <= end: #반복문이 끝나는 시점
    mid = (start + end) // 2 #중간값 잡아주기

    count = 0 #짤린 나무
    for i in tree:
        if i >= mid:
            count += i - mid

    if count >= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)