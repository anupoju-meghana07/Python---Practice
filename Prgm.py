""" 7 x 1=7
    7 x 2=14 """

tab=int(input('Enter a num:'))
for j in range(1,11):
    print(f'{tab} X {j}={tab*j}')

"""-->153=1**3+5**3+3**3"""

num=int(input("Enter a num :"))
length=len(str(num))
amg=0
for j in str(num):
    amg=int(j) ** length + amg
if amg==num:
    print(f'{num} is Amstrong')
else:
    print(f'{num} is not')

"""--> Fibnocci"""

limit=int(input("Enter a limit:"))
num=0
num_2=1
print(num,num_2,end=' ')
for j in range(1,limit+1):
    all_add=num+num_2
    num=num_2
    num_2=all_add
    print(all_add,end=' ')

"""--> Calculator """

num_1=int(input('Enter a num :'))
num_2=int(input('Enter a num :'))
opt=int(input('Enter \n1.Add \n2.Sub \n3.Mul \n4.Div \n5.Mod : '))
if opt==1:
    print(num_1+num_2)
elif opt==2:
    print(num_1-num_2)
elif opt==3:
    print(num_1*num_2)
elif opt==4:
    print(num_1/num_2)
elif opt==5:
    print(num_1%num_2)

"""--> ATM

ICIC_megha={'name':'Megha',
            'ADR':'234567',
            'PAN':'GH3456',
            'ATM PIN':'7700',
            'Balance': 4500}
remain_A=3
while remain_A >0:
    pin=input("Enter your 4 dig Pin:")
    if len(pin)==4:
        if pin in ICIC_megha['ATM PIN']:
            opt=int(input('Enter \n1.Withdraw \n2.Deposite \n3.Balance: '))
            if opt==1:
                    withdraw_m=int(input('Enter amount you want to withdraw :'))
                    if withdraw_m<=ICIC_megha['Balance'] and withdraw_m % 100==0:
                        ICIC_megha['Balance']-=withdraw_m
                        print(f'You have withdraw {withdraw_m} and the total balance {ICIC_megha['Balance']}')
                        break
                    else:
                        print('Can not provide change or no balance')
                        break
            elif opt==2:
                pass
            elif opt==3:
                pass
        else:
            remain_A-=1
            if remain_A>0:
                print(f'Incorrect pin and you have only {remain_A}')
            else:
                print('Card is block')
                break
    else:
        print('Pls enter only 4 digit atm pin')"""




    

