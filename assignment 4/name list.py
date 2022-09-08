#in the name of god

new_list = []
count_list = []
counter = 1
n = int(input('tedad asami mad nazar braye list ra vared : '))

while counter <= n :
    print('Name',counter,':',end ='')
    name1 = str(input())
    new_list.append(name1)
    counter += 1
print()
for name in new_list:
    count = 0
    if name in count_list:
        continue
    else:
        count_list.append(name)
        for i in range(len(new_list)):
            if name == new_list[i]:
                count += 1
    print('tedad esm',name,'=',count)
print()
print('New list :',new_list)
print()
