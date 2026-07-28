""" Functions :
--> Func is block that can be executes when we call it
--> To avoid the repeated lines of code

def function_name(Parameters):
    -----
    -----
    -----
function_name(arguments)

--> Types of Functions:

1 Built-in:

Ex: print(),len(),max(),min()

2 User define :
--> User define are the func that are develop by the user

--> add of two numbers """

num=7
num_2=10
def total_(num,num_2):
    print(num+num_2)
total_(num,num_2)
total_(1,2)

"""--> Sub of two numbers """

num=7
num_2=3
def total_(num,num_2):
    print(num-num_2)
total_(num,num_2)

"""---> Required Arguments:

We have to pass same number arguments that match in the parameters"""

num=10
num_2=5
def total_(num,num_2):
    print(num+num_2)
total_(num,num_2)
total_(1,2,3)

"""--> Positional Arguments:

It does not matter how we are passing the variables , if we assign the value to that variable in the calling """

def Name_(name_,name):
    print(name)
    print(name_)
Name_(name='Megha',name_='Anupoju')

def Alpha_(m,a,b,c,d):
    print(a)
    print(b)
    print(m)
Alpha_(a=0,b=8,c=4,d=1,m=7) 






