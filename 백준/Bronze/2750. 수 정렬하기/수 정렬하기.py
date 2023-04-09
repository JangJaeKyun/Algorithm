n = int(input())

num_up = []
for _ in range(n):
    a = int(input())
    num_up.append(a)

num_set = set(num_up)
num_up = list(num_set)
num_up.sort()

for i in num_up:
    print(i)