from random import random

x = 20
y = []
avg = 0

for i in range(x):
    y.append(random())
    print("%5.2f" %y[i],end='')
    avg += y[i]
print()
avarage = avg/x
print('the avarage of the array = %.2f'% avarage)
for i in y:
    if i> avarage:
        print("%4.2f"% i)