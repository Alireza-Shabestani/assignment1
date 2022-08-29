#in the name of god
counter = 0
import random
adad_pishfarz = random.randint(0, 99)
x = adad_pishfarz
print(30*'-')
print('adad pishfarz : ', x)
print(30*'-')

while True :
    karbar = int(input('please inter your desired number :'))
    if x == karbar :
        counter += 1
        print(30*'-')
        print()
        print('You guessed right, you won')
        print()
        print('number of times the exam : ',counter)
        print()
        print(30*'-')
        break
    elif karbar < x :
        counter += 1
        print(30*'-')
        print('The desired number is bigger...')
        print(30*'-')
    elif x < karbar :
        counter += 1
        print(30*'-')
        print('The desired number is shorter ...')
        print(30*'-')
        