num = list(map(str, input().split()))
num_reverse = []
for i in num:
    num_reverse.append(i[::-1])
print(max(num_reverse))