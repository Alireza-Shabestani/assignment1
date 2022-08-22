#in the name of god

username = 'admin'
password = '102030'

i = 0 

while (i < 3) :
    
    username_karbar = input('please inter your username :')
    password_karbar = input('please inter your password :')

    if (username == username_karbar) & (password == password_karbar) :
        print('Dear user , Login was successful...')
        print('------------------------------------')
    else :
        i = i+1
        print('Dear user , login was failed!!!')
        print('------------------------------------')

print('Your page has been locked , Please try again later....')