str = input('insert some strings of uper and lower case:')

len_str = len(str)

upper = lower = 0

for i in str:
    if 'a' <= i <= 'z':
        lower += 1
    elif 'A' <= i <= 'Z':
        upper += 1
print("persentege of uppercase : %.2f %%"%(upper/len_str * 100))
print("persentege of lowercase : %.2f %%"%(lower/len_str * 100))
