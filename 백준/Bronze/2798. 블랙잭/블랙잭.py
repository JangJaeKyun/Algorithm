import sys
input = sys.stdin.readline

N, M = map(int, input().split())

card_list = list(map(int, input().split()))

anw = []

for i in range(N):
    for j in range(i + 1, N):
        for z in range(j + 1, N):
            if card_list[i] + card_list[j] + card_list[z] > M:
                continue
            else:
                anw.append(card_list[i] + card_list[j] + card_list[z])

print(max(anw))