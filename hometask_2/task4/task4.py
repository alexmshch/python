a = int(input('Введите число: '))
NN = []
for i in range(-a,a,1):
    NN.append(i)

open = open('/Users/aleksejmeserakov/Desktop/Питон GB/hometask_2/task4/file.txt')
f = int(open.read(1))
s = int(open.read(2))
sum = NN[f] * NN[s]
print(sum)