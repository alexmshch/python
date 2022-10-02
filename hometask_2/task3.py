from ast import For


a = int(input('Введите число: '))
sum = 0
while a >= 1:
    number = round((1+1/a)**a)
    sum = sum+number
    a = a-1
print(sum)