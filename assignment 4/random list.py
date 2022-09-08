#in the name of god
import random
counter = 0
random_list = []

tool_list = int(input('The length of the list : '))

while counter < tool_list :
    number = random.randint(-100, 100)
    random_list.append(number)
    counter += 1

print(30*'-')
print('random list :', random_list)
print(30*'-')
