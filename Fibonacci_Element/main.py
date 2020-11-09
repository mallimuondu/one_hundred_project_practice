x = abs(int(input('choose the element to find its value: ')))

f1 = f2 = 1
y=2
while y < x:
    f1,f2 = f2,f1+f2
    y +=1
print("the value of the ",x,"element is = ",f2)