from random import *

names = ['alborz','ardebil','bushehr','azarbaijan','esfahan','fars','gilan',
        'golestan','hamadan','hormozgan','ilam','kerman','kermanshah',
        'khuzestan','kordestan','lorestan','markazi','mazandaran','khorasan',
        'qazvin','qom','semnan','sistan','tehran','yazd','zanjan']								
     
n = randint(0,len(names)-1)
name = names[n]

charNumber = len(name)
userList= ['-'] * charNumber

print(name)   
print(userList)


while userList.count("-") > 0 :

    guess = input(" guess a character: ")

    for i in range(charNumber):
        if guess == name[i] :
            userList[i] = guess

    print(userList)
     
print( " :D - You Win - Congratulations")
