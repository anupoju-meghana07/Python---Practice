""" Modules :

--> Modules are the python code which is saved in (.py) that contain functions,variables,classes

Types:

1.built-in :

--> The built in modules that are already designed which comes with python when we are installing

EX: --> math
    --> sys
    --> os
    --> random
    
2.user-defined :

--> The user defined modules are created by the programmer

Syntax : import(keyword) module_name """


import first_mod
print(first_mod.add(6,8)) 
print(first_mod.subtract(67,8))

"""--> We can also import a module with diff name
--> After importing with the alias name,we have to use that alias name in the code""" 

import first_mod as fm

print(fm.add(6,8)) 
print(fm.subtract(67,8))

"""Importing only needed function

--> When we are importing few functions from the module can only access the func

Syntax:from(keyword) module_name import(keyword) functions """

from first_mod import add,mul

print(add(7,8))
print(mul(7,8))

"""Importing all functions

-->to Use all functions in that module we have to use * to get all of those """

from first_mod import*
print(add(6,8))
print(subtract(8,7))
print(mul(7,9))

import first_mod
first_mod.display()

import random
print(random.randint(1000,4000))

import math
print(math.sqrt(25))

import sys
print(sys.version)

details={'name':'Megha','ATM Pin':'1234'}
import random
remain=3
while remain>0:
    pin=input("Enter pin number: ")
    if pin==details['ATM Pin']:
        otp=random.randint(1000,9999)
        print(otp)
        user_otp=int(input("Enter user otp :"))
        if user_otp==otp:
            opt=int(input("Enter option \n1.Withdraw \n2.Deposit "))
    else:
        remain-=1
        if remain>0:
            print(f"incorrect pin entered and you have{remain}")
        else:
            print(f"You have entered 3 incorrect pins ")
        





