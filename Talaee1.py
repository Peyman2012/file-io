# this program was written by one of my students , "Parham Talebi"

from random import *

print(".-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.")
print(".                                                                     .")
print(".                                                                     .")
print(".                                                                     .")
print(".                                                                     .")
print(".      Hello...!      I AM YOUR SMART PASSWORD GENERATOR   :)         .")
print(".                                                                     .")
print(".                                                                     .")
print(".                                                                     .")
print(".                                                                     .")
print(".                                                                     .")
print(".-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.")

chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
         'w', 'x', 'y', 'z',
         'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
         'W', 'X', 'Y', 'Z',
         '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '+', '=', '!', '@', '$', '%', '^', '&', '*']
print("")
length = int(input("Enter the length of password : "))
print("")
password = ""
for i in range(length):
    x = randint(0, len(chars) - 1)
    password = password + chars[x]
print(password)
