import itertools

n = int(input())

num = map(int, input().split())
nCr = itertools.permutations(num, n)

def calculator(li):
    total = 0
    for i in range(len(li)-1):
        total += abs(li[i]-li[i+1])
    return total

asw = -1e9
for li in nCr:
    asw = max(asw, calculator(li))

print(asw)