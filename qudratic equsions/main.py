import math
x1 = int(input('insert the value of x1:'))
x2 = int(input('insert the value of x2:'))
y1 = int(input('insert the value of y1:'))
y2 = int(input('insert the value of y2:'))
z1 = int(input('insert the value of z1:'))
z2 = int(input('insert the value of z2:'))

x = range(x1, x2+1)
y = range(y1, y2+1)
z = range(z1, z2+1)

for i in x:
    if i == 0:
        continue
    for j in y:
        for k in z:
            print(i,j,k,end = ' ')
            a = j*j-4*i*k
            if a >= 0:
                x1 = (-j - math.sqrt(a))/(2*i)
                x2 = (-j + math.sqrt(a))/(2*i)
                print("VALID", round(x1,2),round(x2,2))
            else:
                print('invalid')