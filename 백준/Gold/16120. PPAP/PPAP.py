n = input().rstrip()
stack = []
ppap = ['P', 'P', 'A', 'P']

for i in range(len(n)):
    stack.append(n[i])
    if stack[-4:] == ppap:
        for _ in range(4):
            stack.pop()
        stack.append('P')

if len(stack) == 0 or stack == ['P']:
    print('PPAP')
else:
    print('NP')
