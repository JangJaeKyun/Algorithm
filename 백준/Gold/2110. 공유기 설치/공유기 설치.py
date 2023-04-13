n, c = map(int, input().split())

x = []
for _ in range(n):
    y = int(input())
    x.append(y)

x.sort()

def binarySearch(x, start, end):
    while start <= end:
        mid = (start + end) // 2
        current = x[0]
        count = 1

        for i in range(1, len(x)):
            if x[i] >= current + mid:
                count += 1
                current = x[i]

        if count >= c:
            global answer
            start = mid + 1
            answer = mid
        else:
            end = mid - 1

start = 1
end = x[-1] - x[0]
answer = 0

binarySearch(x, start, end)
print(answer)