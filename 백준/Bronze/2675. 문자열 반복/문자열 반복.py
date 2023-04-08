s = int(input())

for i in range(s):
    num1, num2 = input().split()
    text = ""
    for i in num2:
        text += int(num1) * i
    print(text)