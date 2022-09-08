#in the name of god 

number = int(input('please inter your desired number : '))

sum = 1
x = 1

while sum < number :
    sum *= x
    x += 1

if sum == number :
    print(30*'-')
    print("The desired number is the factorial of the number : ",x)
    print(30*'-')
else :
    print(30*'-')
    print('sorry...\nThe number you are looking for is not a factorial number')
    print(30*'-')
