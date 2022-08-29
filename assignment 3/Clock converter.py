#in the name of god
print('Hello, dear user')
print('First, select the desired option from the menu below')
print(30*'-')
print('1.convert hour to second')
print('2.convert second to hour')
number = int(input('Select 1 or 2 ? : '))

if number == 1 :
    print('Enter the hour please')
    hour = int(input('hour : '))
    minutes = int(input('minutes : '))
    seconds = int(input('seconds : '))
    print(30*'-')
    convert = (hour*3600)+(minutes*60)+(seconds)
    print('seconds = ',convert)
    print(30*'-')

elif number == 2 :
    print('Enter the seconds please')
    seconds = int(input('seconds : '))
    second=seconds%60
    hour=seconds//3600
    minute=seconds//60-hour*60
    print("time: ",hour,"saat",minute,"daghigheh",second,"sanieh ")