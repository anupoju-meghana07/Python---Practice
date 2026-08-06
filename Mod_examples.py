
"""-->asscii letters : This string module func that can give 
      upper and lower letter
   -->digits:string module func that can give number(0-9)
   -->punctuation:this string moduke func can give us punctuation (&$@) """

import string
print(string.ascii_letters)
print(string.digits)
print(string.punctuation)

#Random Password

import random
import string
letters=string.ascii_letters
digits=string.digits
punctuation=string.punctuation
all_char=letters+digits+punctuation
password=''
for i in range(5):
    password+=random.choice(all_char)
print(password)

#Random Passowrd Generator using spl char

import random
import string
letters=string.ascii_letters
digits=string.digits
spl_char='@#&%'
all_char=letters+digits+spl_char
password=''
for i in range(5):
    password+=random.choice(all_char)
print(password)

#Printing Date and Time 

bank_balance=10000
from datetime import datetime
import sys
now=datetime.now()
while True:
    print("--Welcome to SBI--")
    user_opt=int(input("\n1.Withdraw \n2.Deposit \n3.Check Balance \n4.Exit"))
    if user_opt==1:
        with_m=int(input('Enter the money you want to withdraw'))
        if with_m > bank_balance:
            bank_balance-=with_m
            print(f'remaining money {bank_balance} {now.strftime('%H:%M %Y-%m-%d')}')
        else:
            print("Insufficient money")
    elif user_opt==2:
        Deposite_m=int(input("Enter the money you want to deposite"))
        bank_balance+=Deposite_m
        print(f'Money added successfully : {bank_balance} {now.strftime('%H:%M %Y-%m-%d')}')

    elif user_opt==3:
        print(f"available balance {bank_balance} {now.strftime('%H:%M %Y-%m-%d')}")
    elif user_opt==4:
        sys.exit()
    else:
        print("Incorrect choice")
        print("Thank you for using ATM") 
        sys.exit()
        
#Generating Random number Game

import random
num=random.randint(1,100)
user_opt=int(input("Enter number(1-100)"))
if user_opt==num:
    print(f'You have picked {user_opt} number')
else:
    print('Better luck next time')
    


