#in the name of god
numbers = []
counter = 0
counter1 = 0

for i in range(10):
    number = int(input('please inter your number : '))
    numbers.append(number)

for j in range(9) :
    if numbers[j] <numbers[j+1] :
        counter += 1
        continue
    elif numbers[j] > numbers[j+1] :
        counter1 += 1
        continue
    else :
        break

if counter==10 or counter1==10 :
    print ('yes')
else:
    print ('no')
    
