"""  Set
--> Set is an unordered collection
--> Set does not allows duplicate values inside it
--> Set is muttable
--> set is represented in {}"""

#Duplicates are not allowed
do={1,2,3,2}
print(do)

#To create empty set:
so=set()
print(type(so))

"""----Methods----

--> update(): Use to add new values into set
    Syntax: variable_name.update(iterable)"""

do={1,2,3}
do.update([6,8]) #It takes only iterables
print(do)

do={1,2,3}
do.update('python') #unordered so o/p will be unordered
print(do)

"""--> add(): use to add new value into set, it will take any value
       Syntax: variable_name.update(value)"""

do={1,2,3}
do.add('Python')
print(do)

"""--> remove(): It is use to del the value from the set , incase if the value is not present in the set then it will throw key error
       Syntax: variable_name.remove(value)"""

do={1,2,3,4}
do.remove(4)
print(do)

"""--> discard(): It is use to delete the value from the set but it never gives any error in case if the value is not present inside the set
       Syntax: variable_name.discard(value)"""

do={1,2,3,4}
do.discard(4)
print(do)

"""--> pop(): Used to delete the value but this pop() will take 0 arguments inside it(it will not take any value)
              It will remove the value on its own since it is unordered
              If we give arguments it will throw Position argument error

      Syntax: variable_name.pop()"""


do={1,2,3,4}
do.pop()
print(do)

"""----------Operations-------

--> union(|):(It maps 2 sets together)Gives all set value together but no duplicants"""

do={1,2,5}
so={3,4,5}
print(do|so)
print(do.union(so))

"""--> intersection(&): It gives Common values present in both the sets """

do={1,2,5}
so={3,4,5}
print(do|so)
print(do.intersection(so))

"""--> difference(-):"""

do={1,2,3}
so={3,4,5}
print(so-do)
print(so.difference(do))

"""                                                 Type Conversions
                                                ----------------------

--> Int:

string--str()"""

num=9
print(type(num))#int
so=str(num)
print(type(so))#str

""" Float-- float()"""

num=9
print(type(num)) #int
so=float(num)
print(so)
print(type(so)) #float

"""--> Float:

string--str()"""

nums=9.6
print(type(nums)) #float
all_=str(num)
print(type(all_))#str

""" Integer--int()"""

nums=9.6
print(type(nums)) #float
all_=int(num)
print(all_)
print(type(all_)) #int

"""--> String:

Integer--int()"""

how=" i have 67" # Can't Convert
print(type(how))
who=int(how)
print(type(who))

how=" 67"
print(type(how)) #str
who=int(how)
print(type(who)) #int

"""---> Float--float()"""

how="6.87"   #str
print(type(how)) 
who=float(how)
print(type(who)) #float
      
"""--> List-list """

how='2345'
print(type(how)) #str
who=list(how)
print(who)
print(type(who)) # list

"""--> tuple-tuple"""

how='2345'
print(type(how))  #str
who=(tuple(how))
print(who)
print(type(who))  #tuple

""" --> List

--> string--str() """

nums=[1,2,3,4]
print(type(nums)) #list
all_n=str(nums)
print(type(all_n)) #str

"""--> tuple--tuple()"""

nums=[1,2,3,4]     #list
print(type(nums))
all_n=tuple(nums)  # tuple
print(type(all_n))


"""--> Tuple

--> list--list()"""

nums=(1,2,3,4)
print(type(nums))  #tuple
all_n=list(nums)
print(all_n)
print(type(all_n)) # list

"""--> string--string()"""

nums=(1,2,3,4)
print(type(nums))  #tuple
all_n=str(nums)
print(type(all_n))  #str

"""---------Concatination----

--> (+)"""

num=8
num_2=9
print(num+num_2)

any_='Python is a'
we='Language'
print(any_+we)

nums=[1,2,3]
all_=[3,4]
print(nums+all_)

nums=(1,2,3)
all_=(3,4)
print(nums+all_)






 








 
