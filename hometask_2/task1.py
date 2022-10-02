a = float(input("Введите число"))
from math import floor
sum = 0

while (a-floor(a) > 0):
    a = a*10
print(a)
while (a>10):
    b = a%10
    a = floor(a/10)
    sum = sum+b
sum = sum + a


print(sum)