""" --> elif

1.Grades of marks """

marks_=int(input("Enter your marks: "))
if marks_>=90:
    print('A+')
elif marks_>=80:
    print('A')
elif marks_>=70:
    print('B')
elif marks_>=60:
    print('B')
elif marks_>=50:
    print('C+')
elif marks_>=40:
    print('C')
else:
    print('fail')

"""2.Greatest Among three"""

num=40
num_2=89
num_3=7
if num>num_2 and num>num_2:
    print(f'{num} is greater value')
elif num_2>num and num_2>num_3:
    print(f'{num_2} is greater value')
else:
    print(f'{num_3} is greater value')

"""--> nested if: If inside the if

1. ATM PIN"""

detail_={'ATMPIN':'9870'}
atm_=input('Enter your pin:')
if len(atm_)==4:
    if atm_==detail_['ATMPIN']:
         op_=int(input("Enter \n1.Withdraw \n2.Deposite \n3.Pinchange"))
         if op_==1:
             Money_W=int(input('Enter your Money to withdraw:'))
         elif op_==2:
             Money_D=int(input('Enter Money to Deposite:'))
    else:
        print('Incorrect Pin Entered')
else:
    print('Please Enter Only 4 digit Pin')

"""3.Control Statements:

--> break"""

num=[34,45,56,78,90]
for i in num:
    print(i)
    if i==56:
        break
else:
    print('end')

"""--> Continue:It skips the paticular condition"""

num=[34,45,67,78,90]
for i in num:
    if i==67:
        continue
    print(i)
else:
    print('end')

"""-->Pass: Space Holder( If a statement is incomplete if we put pass after that no error will be raised)
-->It will not throw the error even if the program is incomplete"""

num=[24,45,56,78]
for i in num:
    pass

"""2.Loops :

--> for loop : It is used to iterate over sequence such as str,list,tuple

-->else in for loop it will execute when whole condition(iteration) is completed
-->if condition becomes true then else will never execute
-->range():It gives the sequence of number,Func is used to generate num upto a limit
--> Syntax:
    range(start,end,step)"""

num='Python is a language'
for i in num:
    print(i)

for j in range(1,10,2):
    print(j)

"""--> while loop: """

num=1
while num<=10:
    print(num)
    num+=1

"""Assert Keyword:

--> The keyword is to check the condition
--> we can frame the error
-->After condition what we write that will show as error(if cond fails)"""

age=15
assert age>=18,'Not Eligible'
print('Eligable') #AssertionError: Not Eligible """

marks_=5
assert marks_>=35,'fail'
print('pass') #AssertionError: fail







    
         
         
        



