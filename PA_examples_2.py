import math
import random
 
a = ["Obscure", "Sober", "Vengeful", "Profane", "Bestial", "Undead"]
b = ["Angel", "Burial", "Funeral", "Chaos", "Slime", "Lobotomy", "Daemon"]
 
 
while True:
    try:
        i =random.randint(0, 10) #Take a random pick
        a = a[i] #Get the name
        break
    except:
        pass # Oh no
 
while True:
    try:
        i =random.randint(0, 10) #Take a random pick
        b = b[i] #Get the name
        break
    except:
        pass # Oh no
 
e = ""
for c in a:
    d = ""
    if c == 'o':
        d = 'ö'
    if c == 'u':
        d = 'ü'
    if d != "":
        e += d
    else:
        e += c
 
e += " "
for c in b:
    d = ""
    if c == 'o':
        d = 'ö'
    if c == 'u':
        d = 'ü'
    if d != "":
        e += d
    else:
        e += c
 
print("Your new metal band's name is " + e)

#

import random
 
adjective = ["Obscure", "Sober", "Vengeful", "Profane", "Bestial", "Undead"]
noun = ["Angel", "Burial", "Funeral", "Chaos", "Slime", "Lobotomy"]

index = random.randint(0, 5)
adjective = adjective[index]
noun = noun[index]

full_name = ""
adjective_list = [letter for letter in adjective]
for index in range(len(adjective_list)):
    if adjective_list[index].lower() == "o":
        adjective_list[index] = "ö"
    if adjective_list[index].lower() == "u":
        adjective_list[index] = "ü"
full_name += ("".join(adjective_list)).capitalize()
full_name += " "

noun_list = [letter for letter in noun]
for index in range(len(noun_list)):
    if noun_list[index].lower() == "o":
        noun_list[index] = "ö"
    if noun_list[index].lower() == "u":
        noun_list[index] = "ü"
full_name += "".join(noun_list)

print("Your new metal band's name is " + full_name)
