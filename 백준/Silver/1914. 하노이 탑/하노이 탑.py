import sys
sys.setrecursionlimit(10**8)

def hanoi(n: int, x: int, y: int):

    if n == 1:
        print(x, y)
        return

    if n > 1:
        hanoi(n - 1, x, 6 - x - y)

    print(x, y)

    if n > 1:
        hanoi(n - 1, 6 - x - y, y)



n = int(sys.stdin.readline())

hanois = (2 ** n - 1)
print(hanois)

if n <= 20 :
    hanoi(n, 1, 3)