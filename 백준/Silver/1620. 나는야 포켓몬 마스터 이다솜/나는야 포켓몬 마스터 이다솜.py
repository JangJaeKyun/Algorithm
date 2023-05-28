import sys
input = sys.stdin.readline

N, M = map(int, input().split())

pokemon = {}
pokemon_reverse = {}
for i in range(N):
    name = input().rstrip()
    pokemon[name] = i + 1
    pokemon_reverse[i + 1] = name

for _ in range(M):
    choice = input().rstrip()
    if choice.isdigit():
        number = int(choice)
        print(pokemon_reverse.get(number))
    elif choice.isalpha():
        print(pokemon.get(choice))