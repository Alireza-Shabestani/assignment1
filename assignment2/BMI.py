#in the name of god

vazn = float(input('lotfan vazn khod ra bar hasb Kilogram vared konid : '))
ghad = float(input('lotfan ghad khod ra bar hasb meter vared konid : '))

bmi =(vazn/(ghad*ghad))

if (16 <bmi< 18.5) :
    print('----------------------')
    print('body weight deficit- you need to gain your weight')
elif (18.5 <=bmi< 24) :
    print('----------------------')
    print('norm- you are normal')
elif (24 <=bmi< 30) :
    print('----------------------')
    print('weight over-your close to overweight')
elif (30 <=bmi< 35) :
    print('----------------------')
    print('obesity first degree- you are a little overweight')
elif (35 <=bmi< 40) :
    print('----------------------')
    print('obesity second degree- you are a overweight')
elif (40 <=bmi) :
    print('----------------------')
    print('obesity third degree- your weight is too much!!! ')
else :
    print('------------------------------------------------')
    print('information is incorrect _ please try again ....')

print('your bmi is : ',bmi)
print('-------------------------------------------------------')