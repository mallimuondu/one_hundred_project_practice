# hard way(more lines)

#x = [6,8,9,10,[3,6,4],'t','tt','u',5]
#y = [8,19,6,[3,6,4],'tt','u','z']
#z = []
#
#for i in x:
#    for j in y:
#        if i == j:
#            z.append(i)
#            break
#print(z)


#easy way

x = [6,8,9,10,'t','tt','u',5]
y = [8,19,6,'tt','u','z']


z = list(set(x and set(y)))
print(z)