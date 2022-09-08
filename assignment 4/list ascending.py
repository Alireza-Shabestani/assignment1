#in the name of god

data_list = []
new_list = []

for i in range(10) :
    print('please inter',i+1,'th number : ',end='')
    number = int(input())
    data_list.append(number)

while data_list:
    minimum = data_list[0] 
    for x in data_list: 
        if x < minimum:
            minimum = x
    new_list.append(minimum)
    data_list.remove(minimum)    

print(30*'-')
print (new_list)
print(30*'-')
