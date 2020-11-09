str = input('INSERT A STR:')
len_str = len(str)

for i in range(len_str//2):
    if str[i] != str[-1-i]:
        print("this is NOT a palimdraw")
        exit()
    else:
        print('this is  a palindraw')
        
    break