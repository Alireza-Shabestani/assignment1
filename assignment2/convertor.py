#in the name of god

meghyas1 =str(input('meghyas aval ra vared konid :'))
meghyas2 =str(input('meghyas dovom ra vared konid :'))

temperature =float(input('dama ra bar hasb meghyas aval vared konid :'))

if((meghyas1=="K" or meghyas1=="F" or meghyas1=="C")and(meghyas2=="C" or meghyas2=="F" or meghyas2=="K")):

    if(meghyas1=="F"and meghyas2=="C"):
        res=((temperature-32) * 5/9 )

    elif(meghyas1=="F" and meghyas2=="K"):
        res=((temperature-32) * 5/9 )+ 273.15

    elif(meghyas1=="K" and meghyas2=="C"):
        res=(temperature-273.15 )
        
    elif(meghyas1=='K' and meghyas2=="F"):
        res=((temperature -273.15) * 9/5) + 32 

    elif(meghyas1=="C" and meghyas2=="K"):
        res=(temperature+273.15 )

    elif(meghyas1=="C" and meghyas2=='F'):
        res=(temperature*9/5) + 32 

    print('---------------------------------------------')
    print(t,"darajeh",meghyas1,"=",res,"darajeh",meghyas2)
    print('---------------------------------------------')


else:
    print('---------------------------------------------')
    print("meghyas vared shode nadorst ast!!!")
    print('---------------------------------------------')




