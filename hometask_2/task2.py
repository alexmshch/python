a = int(input('Введите число'))
sum = a
b = a
sum2 = 1

while (a > 1):
    a = a-1
    print((sum),end=',')
    sum = sum*a
    
print(sum)

counter = 1
while (counter < b):
    counter = counter+1
    print((sum2),end=',')
    sum2 = sum2*counter
    
print(sum2)