n = int(input())

arr = []
for _ in range(n):
    w = input()
    arr.append(w)

arr_set = set(arr)
arr = list(arr_set)
arr.sort(key=lambda x : (len(x), x))
for i in arr:
    print(i)
