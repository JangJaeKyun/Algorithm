import sys
input = sys.stdin.readline

def sosoo(t):
	# 소수 체크 #
	flag = True
	i = 2
	while i * i <= t: 
		if t % i == 0:
			flag = False
			break
		i += 1
 
	if flag:
		for i in range(1,10):
			sosoo(t*10 + i)
	else: return

	if len(str(t)) == N:
		print(t)
		return
	
N = int(input())
for i in range(2,10):
	sosoo(i)