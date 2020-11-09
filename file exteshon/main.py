exe = ['gif','png','jpeg','jpg','svg','txt']

filex = input('insert file with exstosion: ').split('.')
if len(filex) >= 2:
    extension = filex[-1].lower()
    if  extension in exe:
        print("file exetension exists")
    else:
        print('file extension does not exist')
else:
    print("file does not have an extension")