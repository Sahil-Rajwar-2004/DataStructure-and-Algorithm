num = int(input("number of series: "))
a = 0
b = 1

for i in range(num):
    print(a)
    c = a+b
    a,b = b,c
