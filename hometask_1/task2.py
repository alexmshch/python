a = int(input("Введите число 1: "))
b = int(input("Введите число 2: "))
c = int(input("Введите число 3: "))

left = not (a or b or c)
right = not a and not b and not c

if left == right:
    print ('true')
else:
    print('false')