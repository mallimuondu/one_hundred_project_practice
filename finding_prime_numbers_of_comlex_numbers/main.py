import math
def main():
    x = int(input('insert any number to check: '))
    if x < 2:
        print('pls insert number greaiter than two or equal to 2.try again')
        main()
    elif x == 2:
        print('this is a prime number')
        exit()
    y = 2
    num = int(math.sqrt(x))
    
    while y <= num:
        if x%y == 0:
            print('this is a complex number')
            exit()
        y += 1
    print("this is a prime number")
main()
    