a = int(input('Введите X: '))
b = int(input('Введите Y: '))

if a == 0 and b == 0:
    print('начало координат')
if a > 0:
    if b > 0:
        print('1')
    else:
        print('4')
else:
    if b > 0:
        print('2')
    else:
        print('3')