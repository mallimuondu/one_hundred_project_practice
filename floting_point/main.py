from random import random

x = float(input('enter a number to find the maximum floting point:'))

#print(x)

y = str(x)
mxi = -1

for i in range(len(y)):
    if y[i] == '.':
        continue
    elif mxi < int(y[i]):
        mxi = int(y[i])
print('the maximum element is = ',mxi)