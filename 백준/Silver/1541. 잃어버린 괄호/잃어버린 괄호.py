import sys
input = sys.stdin.readline

n = input().split('-')  # 입력값을 -기준으로 나눠 저장
num = []

for i in n:  # 분리된 문자열에 대해 반복문 수행
    count = 0  # 각 문자열에서 숫자들의 합을 계산하기 위한 변수 초기화
    m = i.split('+')  # '+'를 기준으로 숫자를 분리하여 리스트로 저장
    for j in m:  # 분리된 숫자들에 대해 반복문 수행
        count += int(j)  # 각 숫자들을 정수형으로 변환하여 더함
    num.append(count)  # 각 문자열의 숫자들의 합을 결과값 리스트에 저장

k = num[0]  # 첫 번째 숫자를 변수 k에 저장
for i in range(1, len(num)):  # 첫 번째 숫자 이후의 숫자들에 대해 반복문 수행
    k -= num[i]  # 첫 번째 숫자에서 다른 숫자들의 합을 뺌

print(k)  # 결과값 출력