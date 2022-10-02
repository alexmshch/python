elements = int(input('Введите число: '))
import random
NN = []
r = elements*5
for i in range(0,r,5):
    NN.append(i)
    
counter = 0
while counter < elements:
    randnumber1 = random.randint(0,elements-1)
    randnumber2 = random.randint(0,elements-1)
    save = NN[randnumber1]
    NN[randnumber1] = NN[randnumber2]
    NN[randnumber2] = save
    counter = counter + 1
    
print(NN)