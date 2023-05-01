# 첫째 줄에 멀티탭의 구멍 개수 N, 전기 용품의 총 사용횟수 K(테이블 케이스)가 주어짐
# 둘째 줄에 전기용품의 이름이 K이하의 자연수로 사용 순서대로 한 줄로 주어진다
# 하나씩 플러그를 빼는 최소의 횟수를 출력하라

# 전기용품 사용 순서를 리스트에 넣고
# 사용중 리스트에 전기용품 사용 순서 리스트의 앞부터 멀티탭의 구멍 개수 만큼 옮김
# 멀티탭의 구멍 수 만큼의 숫자를 다시 꺼내서 사용중 리스트와 비교
# 없는 숫자가 있으면 바꾸고 카운트 + 1
# 카운트 출력(가능?)
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

# 전자제품 리스트 입력받기
electronic = list(map(int, input().split()))

# 현재 꽂혀있는 전자제품 리스트 초기화
multitap = [0] * N
# for i in range(N):
#     if electronic[i] not in multitap:
#         multitap[i] = electronic[i]


# 총 뽑아내야 하는 횟수를 나타내는 변수
count = 0

# 꽂아야 할 전자제품 리스트를 탐색하면서 꽂아야 할 전자제품이 이미 멀티탭에 꽂혀있는지 확인
for i in range(K):
    if electronic[i] in multitap:
        continue
    if 0 in multitap:
        multitap[multitap.index(0)] = electronic[i]
        continue
    if electronic[i] not in multitap:
        for j in range(len(multitap)):
            if multitap[j] not in electronic[i + 1:]:
                multitap[j] = electronic[i]
                count += 1
                break
        else:
            # 멀티탭에 빈 플러그가 없으면 가장 나중에 사용되는 전자제품을 뽑아내기
            farthest = 0 # 사용이 가장 늦게 일어나는 전자제품을 찾기 위한 변수
            for j in range(len(multitap)):
                idx = electronic.index(multitap[j], i+1) # 가장 나중에 사용되는 전자제품의 인덱스 구하기
                if idx > farthest: # 현재까지 구한 가장 늦게 사용되는 전자제품보다 더 늦게 사용될 전자제품을 찾으면
                    farthest = idx # 가장 늦게 사용되는 전자제품 갱신
                    farthest_idx = j # 해당 전자제품이 멀티탭에서 몇 번째 플러그에 꽂혀 있는지 저장
            multitap[farthest_idx] = electronic[i] # 해당 전자제품으로 교체
            count += 1
            
print(count)
