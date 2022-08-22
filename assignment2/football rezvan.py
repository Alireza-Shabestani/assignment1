#in the name of god

win = 0
draw = 0
lose = 0
print('Choose according to the menu below :')
print('1.win')
print('2.draw')
print('3.lose')
print('--------------------------------------')
h1 = int(input('The result of the first home game :'))
if h1==1 :
    win+=1
elif h2 == 2 :
    draw+=1
else :
    lose+=1
h2 = int(input('The result of the second home game :'))
if h2==1 :
    win+=1
elif h2 == 2 :
    draw+=1
else :
    lose+=1
h3 = int(input('The result of the third home game :'))
if h3==1 :
    win+=1
elif h3 == 2 :
    draw+=1
else :
    lose+=1
w1 = int(input('The result of the first away game :'))
if w1==1 :
    win+=1
elif w1 == 2 :
    draw+=1
else :
    lose+=1
w2 = int(input('The result of the second away game :'))
if w2==1 :
    win+=1
elif w2 == 2 :
    draw+=1
else :
    lose+=1
w3 = int(input('The result of the third away game :'))
if w3==1 :
    win+=1
elif w3 == 2 :
    draw+=1
else :
    lose+=1

socer = (win*3) + draw

print()
print('--------------------------------------')

print('Rezvan University football team : ')
print()

print(' matches played      win     draw      lose      socer')
print('---------------------------------------------------------')
print('       5             ',win,'      ',draw,'       ',lose,'       ',socer)