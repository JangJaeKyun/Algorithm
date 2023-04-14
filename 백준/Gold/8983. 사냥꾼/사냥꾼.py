m, n, l = map(int, input().split()) #시대, 동물 수, 사정거리
m_list = list(map(int, input().split())) #사대 좌표
m_list.sort() #정렬
x_y = [list(map(int, input().split())) for i in range(n)] #동물들 x, y 좌표

count = 0
for x, y in x_y: # x, y 에 동물 좌표
    start = 0
    end = len(m_list) - 1 #사대의 개수로 범위 지정
    while start < end: #이분탐색 종료 시점
        mid = (start + end) // 2 # 중간값
        if m_list[mid] < x: #m_list의 중간 인덱스가 x보다 작으면 x보다 mid가 작으므로 스타트지점 옮김
            start = mid + 1
        else:
            end = mid #m_list의 중간 인덱스가 x보다 크면 끝지점 옮김  end의 위치가 x랑 가장 가까운 수가 됨

    if abs(m_list[end] - x) + y <= l or abs(m_list[end-1] - x) + y <= l: #end와 end-1은 a의 왼쪽 오른쪽 값 ㅣxj - ajㅣ + bj <= l 이면 동물을 잡은거니 count +1
        count += 1

print(count)