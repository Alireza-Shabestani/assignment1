#in the name of god
x = 0
number = int(input('please inter your number : '))
adad = number
while adad != 0 :
    x =(x*10)+(adad%10)
    adad = adad//10
print('------------------------')
print('your number :', number)
print('Reverse your number :',x)
print('------------------------')

if number == x :
    print('The desired number is equal to its inverse')
else :
    print('The desired number is not equal to its inverse !!!')