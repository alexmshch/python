a = int(input('Введите четверть: '))

if a == 1:
    print('(+∞;+∞)')
if a == 2:
    print('(-∞;+∞)')
if a == 3:
    print('(-∞;-∞)')
if a == 4:
    print('(+∞;-∞)')
else:
    print('Не система координат')