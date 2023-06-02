import sys
input = sys.stdin.readline

N, M = map(int, input().split())

count = 0
listen_name = set()
see_name = set()
listen_see_name = []
for i in range(N):
    listen_name.add(input().rstrip())

for j in range(M):
    see_name.add(input().rstrip())

listen_see_name = sorted(list(listen_name & see_name))

print(len(listen_see_name))
for i, name in enumerate(listen_see_name):
    if i > 0:
        print()
    print(name, end='')
