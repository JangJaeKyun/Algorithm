import sys
input = sys.stdin.readline

# 'm o o' 문자열을 저장한 리스트 생성
s0 = ['m', 'o', 'o']

# 입력값 n, 블록 개수 k, 현재 문자열 길이 l을 받아서 문자열 'moo' 생성
def moo(n, k, l):
    ls = 2 * l + k + 3  # 다음 블록이 추가된 문자열 길이 계산

    # 만약 n이 3 이하인 경우, s0에서 해당 값을 출력하고 함수 종료
    if n <= 3:
        print(s0[n-1])
        return 0
    
    # 다음 블록이 추가된 문자열 길이가 n보다 작은 경우, 블록 개수 k를 증가시키고 다시 함수 호출
    if ls < n:
        moo(n, k+1, ls)
    else:
        # 현재 위치한 블록에 속한 경우
        if n > l and n <= l + k + 3:
            if n - l != 1:  # 블록 내에서 'o' 출력
                print('o')
            else:  # 블록 내에서 'm' 출력 후 함수 종료
                print('m')
                return 0
        else:  # 다음 블록으로 이동하기 위해 함수 호출
            moo(n - (l + k + 3), 1, 3)

n = int(input()) # 입력값을 받고 moo 함수 호출
moo(n, 1, 3)