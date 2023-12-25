import random
import string
l1=list(string.ascii_lowercase)
l2=list(string.ascii_uppercase)
letters=l1+l2
num=['0','1','2','3','4','5','6','7','8','9']
sym=['!','@','#','$','%','^','&','*','(',')']

#user inputs
Letters=int(input("Input how many of letters: "))
symbols=int(input("Input how many of symbols: "))
numbers=int(input("Input how many of numbers: "))
password=[]
for char in range(0,Letters+1):
    password.append(random.choice(letters))
for char in range(0,symbols+1):
    password.append(random.choice(sym))
for char in range(0,numbers+1):
    password.append(random.choice(num))

print(''.join(password))
