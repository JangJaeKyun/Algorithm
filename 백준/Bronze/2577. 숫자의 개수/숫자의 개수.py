a = int(input())
b = int(input())
c = int(input())

str_abc = (str(a*b*c))

for i in range(10):
    print(str_abc.count(str(i)))