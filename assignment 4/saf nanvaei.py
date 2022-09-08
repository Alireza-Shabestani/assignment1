#in the name of god

saf_nanvaei = ['ali','atefeh','reza','homa','amir','fatemeh']

for i in range(3):
    print('please inter your name : ',end='')
    name = input()
    print('please inter your intended position :',end='')
    place = int(input())

    saf_nanvaei.insert(place, name)
print(30*'-')
print(saf_nanvaei)
print(30*'-')
