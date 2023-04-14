import sys

n = int(input()) #테이블 테스트 개수
lst = [] #주어진 8개의 리스트
for _ in range(n):
    lst.append(list(map(int, input().split())))

def conqure(n, lst):
    if not any(1 in i for i in lst): #리스트에 1이 없으면
        lst_count.append(0) #lst_count에 0을 넣음
        return
    elif not any(0 in i for i in lst): #르스트에 0이 없으면
        lst_count.append(1) #lst_count에 1을 넣음
        return
    else:
        lst_0 = [] #리스트 2개를 만들어서
        lst_1 = []
        for i in lst:
            lst_0.append(i[:n//2]) #세로 반으로 나눠버림
            lst_1.append(i[n//2:]) #나머지 반
        conqure(n//2, lst_0[:n//2]) #그걸 또 반으로 나눔
        conqure(n//2, lst_0[n//2:])
        conqure(n//2, lst_1[:n//2])
        conqure(n//2, lst_1[n//2:])
        return
    
lst_count = [] #함수안에서 0과 1을 넣을 리스트
conqure(n, lst) #함수 호출
print(lst_count.count(0)) #0의 개수 카운트
print(lst_count.count(1)) #1의 개수 카운트