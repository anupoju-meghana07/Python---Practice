"""
POP : Procedural Oriented Programming --> Dividing the entire code into blocks
Functions-->A reusable block of code ( A block of statements which performs a specific task)

Syntax:
def funcname (parameters): #Func def
              Doc String
            statements....   #body of func
            ......
            return value(s)
fname(args) #Func Call """

#Addition 

def add(a,b): 
    """addition func"""
    c=a+b
    return c
print(add(5,6))
c,d="Codegnan","Python"
print(add(c,d))
e,f=map(str,input("Enter the value:").split(','))
print(add(e,f))
print(add([1,3,4],[4,6,7])) #Merging
#print(add(1,2,3,4))        #Positional Arguments fail 

#Variable Length Arguments --> *args We can pass any number of postional
#Arguments--> Data will will be stored in tuple 

def sample(*a):
    """Demo of Variable_length arguments """ 
    print(a)
    print(type(a))  #default it stores in tuple format
sample()
sample(2,3,4,5)
sample('codegnan',[23,4],'poll',2+7j)

marks=[20,90,25,18]
sample(marks)      #LEN=1
sample(*marks)     #Access one by one (len=4)

a,*b,c=10,'code','poll',23,4,9
print(a) #10
print(b) #['code', 'poll', 23, 4]
print(c) #9

#*a is used to unpack the values into a collection 

def add(*a):
    """Perform add for numeric values """
    print(a)
    result=0
    for i in a:
        #print(i)
        result=result+i
    return(result)
print(add(7,9,8))

#It Should accept only integer,float data types 

def add(*a):
    print(a)
    result=0
    for i in a:
        #if type(i) in [int,float]:
        if type(i) == int or type(i) == float:
            result=result+i
    return(result)
print(add(add(7,'megha',3,4)))  

#keyword arguments  --> we can pass the name for the arguments 

def batch(name,age,place):
    """Keyword arguments usage """ 
    print(f'{name} is in {place} and age is {age} years')
batch(place='Vizag',name='Codegnan',age=1) 
#Keyword arguments only needs name matching not order 

#Default Arguments :

def batch(name,age,place="Vizag"):
    print(f'{name} is in {place} and age is {age} years')
batch(name='Codegnan',age=1)
"""
#Parameter without default always follows parameter with follow  : We can not make the first one as default

def batch(name="codegnan",age,place):
     print(f'{name} is in {place} and age is {age} years')
batch(age=1,place="vizag",)

print(4,5) 
print(4,5,sep=':') #Here keyword arguments is sep and we are changing the default value for sep

#Keyword Variable Length arguments (**kwargs) --> Any number of
#Keyword arguments,data is stored in dict """

def batch(**a):
    """Keyword Variable length argumentss usage""" 
    print(a)
    print(type(a))
batch()
batch(name="Megha",age=21,place="vizag",branch="CSE")
data={'names':['AKash','Praneeth'],'place':['Vizag','Rajamundry']}
data.update({'batch':'PFS-VSP-007'})
batch(**data)
"""
#Task:Create a func with the usage of *args & **kwargs


def fn(*a,**b):
  ...
  ...
fn(*c,**d) """




    

            
        





