#in the name of god

#number = int(input('lotfan tas ra partab konid : '))

import random
x = random.randint(1,6)
sum = 0
adad_tas=[6]
sum += x
while x == 6 :
    x = random.randint(1, 6)
    adad_tas.append(x)
    sum += x
if sum <6 :
    print('adad tas : ', x)
else :
    print(adad_tas)
print('majmoue adad : ',sum)
print(10*'-')

