"""                         Output Formatting

1.comma seperation """

name='Megha'
age=45
print('Welcome',name,'Your age is',age)

"""2.F-String (doc-string)"""

name='Megha'
age=45
print(f'Welcome {name} your age is {age}')

"""3.Modulas

%s--> all"""

name='Sony'
print('name: %s' % name)


"""%d--> digit"""

price=89.0
print('name: %f' % price)


"""%f--> float"""

price=89.0
print('name: %f' % price)

"""5. (dot)format """

name='Sony'
age=89
print('name:{} age:{}'.format(name,age))

name='Sony'
age=89
print('name:{} \nage:{}'.format(name,age))



"""---------------------------------------------  Statement ------------------------------------------------
1. Condition

--> if
--> if else
--> elif
--> nested if


2.Control

--> break
--> continue
--> pass

3.Loop

--> while
--> for

1.Condition

--> if: The if condition is used to check if it is true or false"""

age=int(input("Enter your age"))
if age>=18:
    print(f"your age is {age} and eligible to vote")

"""--> if else: else is the fall back statement , incase if condition is false then this else block will execute """

age=int(input("Enter your age: "))
if age>=18:
    print(f"your age is {age} and eligible to vote")
else:
    print(f"your age is {age},you have to wait {18-age} years") 

"""--> Even or odd """

num=int(input("Enter a number:"))
if num%2==0:
    print(f"{num} is a even num")
else:
    print(f"{num} is a odd num")

"""--> Vowel or not"""

vol_= input('Enter a single letter:')
if vol_ in 'AEIOUaeiou':
    print(f'{vol_} is vol')
else:
    print(f'{vol_} is con')

"""--> Palindrome"""

so='megha'
if so[::-1] == so:
    print(f"{so} is palindrome")
else:
    print(f"{so} is not palindrome")

"""--> Leap year or not"""

year=int(input("Enter a year:"))
if year%4==0 and year%100!=0 or year%400==0 :
    print(f'{year} is a leap year')
else:
    print(f'{year} not a leap')

"""-->  Mobile is Indian or Not"""

mobile=input('Enter your mobile num')
length=len(mobile)
if length==10:
    print(f'{mobile} is an Indian Num')
else:
    print(f'{mobile} is not an Indian Num')


























































