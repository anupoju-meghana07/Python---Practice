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

Syntax : import(keyword) module_name 


import first_mod
print(first_mod.add(6,8)) 
print(first_mod.subtract(67,8))

--> We can also import a module with diff name
--> After importing with the alias name,we have to use that alias name in the code

import first_mod as fm

print(fm.add(6,8)) 
print(fm.subtract(67,8))

Importing only needed function

--> When we are importing few functions from the module can only access the func

Syntax:from(keyword) module_name import(keyword) functions 

from first_mod import add,mul

print(add(7,8))
print(mul(7,8))

Importing all functions

-->to Use all functions in that module we have to use * to get all of those 

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
            print(f"You have entered 3 incorrect pins ")  """


"""1. Math():

-->math module used to work on mathematical functionality

--> floor
It will round down to near value """

import math
print(math.floor(3.78))

"""-->ceil
It will round up to near value """

import math
print(math.ceil(3.78))

"""-->gcd
It will find the gcd value"""

import math
print(math.gcd(24,36))

"""-->LCM
It will find the lcm value"""

import math
print(math.lcm(24,36))

"""-->Sqrt
It will find the square root value """ 

import math
print(math.sqrt(25))

"""-->Factorial:
It will give factorial value """

import math
print(math.factorial(5))

"""-->Log """

import math
print(math.log(2,3))
print(math.cos(math.pi))
print(math.pi)

"""2.Random :
The random module used to get the random number

--> randint
It is used to generate random numbers based on range """

import random
print(random.randint(1,100))

"""--> choice
It will select the random value from the data

--> Shuffle
It can shuffle the data randomly """

import random
color = ['black','blue','yellow']
print(random.choice(color))
random.shuffle(color)
print(color)

"""--> Uniform
It will give decimal values in a givenrange """

import random
print(random.uniform(1,100))

"""3.sys 
Sys module is used to give details of python interpreter

--> Version
will get version of python interpreter """

import sys
print(sys.version)

"""-->Path 
.py path we will get by this func """

import sys
print(sys.path)

"""--> exit
This func will exit from the program """

import sys
print(sys.exit())

"""--> Platform
It will gives the python run platform """

import sys
print(sys.platform)

"""-->argv
It will give current file run path """

import sys
print(sys.argv)

"""-->datetime
Used to work with date and time

--> now
It will give the today time+date  """

from datetime import datetime
print(datetime.now())

"""-->%Y:will get the year
-->%m:will get the month
-->%d:will get the day
-->%H:will get the hour
-->%m:will get the minute
-->%S:will get the seconds
-->%A:will get the current day
-->%B:will get the current month  """


from datetime import datetime
now=datetime.now()
print(now.strftime('%Y-%m-%d'))
print(now.strftime('%Y-%m'))
print(now.strftime('%A'))
print(now.strftime('%B'))
print(now.strftime('%H:%M:%S'))

"""4.Collections

--> The collections module will provide container type data which is more powerful than the built in data types(dic,list,tuple) """

import collections
data=['apple','banana','goa','orange','banana']
print(collections.Counter(data))

"""--> Deque:

Used to work with list """

from collections import deque
how=deque([1,2,3])
how.appendleft(7)
print(how)

from collections import deque
how=deque([1,2,3])
how.extendleft([7,8,9])
print(how) 

from collections import deque
how=deque([1,2,3])
how.pop()
print(how)

from collections import namedtuple
data=namedtuple("stu",('name','age'))
print(data('megha',22))

"""5.Intertools:

-->Count: """

from itertools import count
c=count(100)
for j in range(5):
    print(next(c))

"""-->repeat: """

import itertools
for j in itertools.repeat('Python',10):
    print(j)

"""-->Permutations : """

from itertools import permutations
data=permutations([1,2,3],2)
print(list(data))

"""-->Combinations : """

from itertools import combinations
any=combinations([1,2,3],2)
print(list(any))

"""6. Platform"""

import platform
print(platform.python_version())
print(platform.python_compiler())
print(platform.machine())
print(platform.processor())











 







