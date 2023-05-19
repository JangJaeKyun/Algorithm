import sys
from collections import Counter

# 입력 받기
N = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))

# 카드 숫자 개수 세기
card_counter = Counter(cards)

# 결과 출력
for num in numbers:
    print(card_counter[num], end=" ")