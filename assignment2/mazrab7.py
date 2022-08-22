#in the name of god

number=x=int(input('please inter your number : '))

if (number%7 == 0) :
    print('--------------------------------------')
    print('The desired number is a multiple of 7')
    print('--------------------------------------')

else :
    while (number%7 != 0) :
        number+=1
    print('--------------------------------------')
    print('The first multiple of 7 after the desired number :', number)
    print('--------------------------------------')
