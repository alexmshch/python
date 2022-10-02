a = int(input('Введите число'))
sum = a

while (a > 1):
    a = a-1
    print((sum),end=',')
    sum = sum*a
    
print(sum)