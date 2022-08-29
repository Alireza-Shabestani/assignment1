#in the name of god 

password = 1401
number = 1
ramz = int(input('please inter your password : '))

while number<3 :
    if 1000<=ramz<=9999 :
        if ramz == password :
            print(30*'-')
            print('welcome ...')
            print(30*'-')
            break
        elif ramz == 1041 :
            print(30*'-')
            print('danger!!!...\n''A message was sent to the police...')
            print(30*'-')
            break
        else :
            number+=1
            ramz = int(input('please inter your password : '))
    else :
        ramz = int(input('please inter your password : '))
        continue

if number == 3 :
    print(30*'-')
    print('Your page has been closed')
    print(30*'-')