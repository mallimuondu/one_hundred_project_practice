str = "hello,world,table,chair,cup,tea"
print(str)

substr1 = input('choose an old substring to replace: ')
substr2 = input('INSERT new substring: ')

lensubstr1 = len(substr1)
while str.find(substr1)>0:
    i = str.find(substr1)
    str = str[:i] + substr2 + str[i+lensubstr1:]
print(str)