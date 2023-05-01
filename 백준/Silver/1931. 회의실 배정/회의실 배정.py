import sys
input = sys.stdin.readline

n = int(input())

meeting = []
for i in range(n):
    time = list(map(int, input().split()))
    meeting.append(time)

meeting.sort(key=lambda x: (x[1], x[0]))

end_time = 0
count = 0
# 끝나는 시간이 빠른 순으로 정렬한 후 시작시간과 끝나는 시간을 각각 start와 end 변수에 할당
for start, end in meeting:
    # start가 end_time보다 크거나 같으면 회의실을 사용할 수 있으므로 count 변수에 1을 더해줍니다
    if start >= end_time:
        count += 1
        # 회의의 끝나는 시간 end를 end_time 변수에 저장
        end_time = end

print(count)
