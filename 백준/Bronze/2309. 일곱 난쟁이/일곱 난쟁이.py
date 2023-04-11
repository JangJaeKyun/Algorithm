key_list = []
key_lists = []
aws = []
for _ in range(9):
    key = int(input())
    key_list.append(key)
    key_lists.append(key)

for i in range(9):
    for j in range(i+1, 9):
        del key_lists[j]
        del key_lists[i]
        if sum(key_lists) == 100:
            break
        else:
            key_lists = key_list[:]
    if sum(key_lists) == 100:
        break

key_lists.sort()
for k in key_lists:
    print(k)