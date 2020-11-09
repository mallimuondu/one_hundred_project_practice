str1 = input('insert starting leter: ')
str2 = input('insert ending leter: ')

while str1 <= str2:
    print(str1, end = " ")
    str1 = chr(ord(str1)+1)
print()