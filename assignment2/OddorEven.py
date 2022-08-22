#in the name of god
even = 0
odd = 0

number = int(input('please inter your number : '))
if number == 0 :
    even+= 1
while number != 0 :
    x=number%10
    if x%2==0 :
        even +=1
    else :
        odd+=1
    
    number=number//10

print('-------------------------------')
print('Number of odd digits :' , odd)
print('Number of even digits :' , even)
print('-------------------------------')

if even > odd :
    print('The number of even digits is more than the number of odd digits')
    print('----------------------------------------------------------------')
elif odd > even :
    print('The number of odd digits is more than the number of even digits')
    print('----------------------------------------------------------------')
elif (even == odd) and odd !=0 :
    print('The number of even digits is equal to the number of odd digits')
    print('----------------------------------------------------------------')