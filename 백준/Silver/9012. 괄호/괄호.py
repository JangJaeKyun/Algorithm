# (, {, [, ], }, ) 등 괄호를 받고 올바른 괄호 문자열(vps)면 yes, 아니면 No를 출력

import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    stack = []
    bracket = input().rstrip()
    for i in bracket:
        if i == "(":
            stack.append(i)
        elif i == ")":
            if len(stack) == 0:
                stack.pop
                stack.append(i)
                break
            else:
                stack.pop()
        
    if len(stack) == 0:
        print("YES")
    else:
        print("NO")

            