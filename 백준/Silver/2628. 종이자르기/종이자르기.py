width, length = map(int, input().split())
width_list = [0, length]
length_list = [0, width]

num = int(input())
for _ in range(num):
    tyep, a = map(int, input().split())
    if tyep == 0:
        width_list.append(a)
    elif tyep == 1:
        length_list.append(a)

width_list.sort(reverse=True)
length_list.sort(reverse=True)

result = 0
x = 0
y = 0
for i in range(len(width_list)-1):
    for j in range(len(length_list)-1):
        x = width_list[i]-width_list[i+1]
        y = length_list[j]-length_list[j+1]
        xy = x * y
        result = max(result, xy)

print(result)