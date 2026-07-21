"""  ------ Input Formating-----

--> int: Input format for integer
         int(input())"""

num=int(input('Enter a num:'))
print(num+9)
print(type(num)) #<class 'int'>

""" --> String: input()"""

we=input('Enter:')
print(type(we)) #<class 'str'>

"""--> List: Split:Cuts the string at every space & turns into a list ,
       Map:Converts the elements to numbers(Takes each string in your split list and runs the int() func on it"""

nums=list(map(int,input('Enter nums:').split()))
print(nums) #<class 'str'>

nums=input('Enter nums:').split() #['89', '70']
print(nums)

"""--> Tuple() : eval: It identifies the data type based on our input"""

nums=tuple(map(int,input('enter nums :').split()))
print(nums) #(56, 70)

nums=eval(input('Enter num:'))
print(type(nums)) #<class 'int'>

""""--> python(Reverse)"""

name="Python"
print(name[::-1])  #nohtyP

"""-->Covert 23:56--11.56 pm """

time=input("Enter a 24H clock :")
parts=time.split(':')  #23:56
Hours=int(parts[0])-12
print(Hours,':',parts[1],'pm') #11 : 56 pm







