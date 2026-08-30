#ATM machine
ICIC_Megha={'name':'megha',
            'ADR':'78956789',
            'PAN':'MVK234RTY',
            'ATM PIN':'7700',
            'BALANCE':4500,
            'Transaction':[]}

print("Please insert your ATM card")
import random
remain_A=3
while remain_A>0:
    pin=input('enter your 4 digit pin:')
    if len(pin)==4:
        if pin in ICIC_Megha['ATM PIN']:
            otp=random.randint(1000,9999)
            print(otp)
            user_otp=int(input("Enter user otp :"))
            option=int(input('Enter \n1.Withdraw \n2.Deposit \n3.Balance \n4.Exit:'))
            if option==1:
                withdraw_m=int(input('Enter amount you want to withdraw:'))
                if withdraw_m<=ICIC_Megha['BALANCE'] and withdraw_m%100==0:
                    ICIC_Megha['BALANCE']-=withdraw_m
                    ICIC_Megha['Transaction'].append(f'withdraw:-{withdraw_m}')
                    print(f'you have withdraw {withdraw_m} and the total balance {ICIC_Megha['BALANCE']}')
                    user=int(input('Enter \n1.Home page \n2.Exit:'))
                    if user==1:
                        print('Home page')
                    else:
                        print('Thank you for visiting')
                else:
                    print('can not provide change or no balance')
                    user=int(input('Enter \n1.Home page \n2.Exit:'))
                    if user==1:
                        print('Home page')
                    else:
                        print('Thank you for visiting')
            elif option==2:
                deposit_m=int(input('Enter the money you want to deposit:'))
                if deposit_m%100==0:
                    ICIC_Megha['BALANCE']+=deposit_m
                    ICIC_Megha['Transaction'].append(f'deposit:+{deposit_m}')
                    print(f'you have deposited {deposit_m} and the total balance{ICIC_Megha['BALANCE']}')
                    user=int(input('Enter \n1.Home page \n2.Exit:'))
                    if user==1:
                        print('Home page')
                    else:
                        print('Thank you for visiting')
                        user=int(input('Enter \n1.Home page \n2.Exit:'))
                        if user==1:
                            print('Home page')
                        else:
                            print('Thank you for visiting')
                else:
                    print('change can not deposit')
                    user=int(input('Enter \n1.Home page \n2.Exit:'))
                    if user==1:
                        print('Home page')
                    else:
                        print('Thank you for visiting')
            elif option==3:
                print(f'Your Current Balance:{ICIC_Megha['BALANCE']}')
                print('Transaction History:',ICIC_Megha['Transaction'])
            elif option==4:
                print('Thank you for visiting ICIC')
                break
            else:
                print('Invalid option')      
        else:
            remain_A-=1
            if remain_A>0:
                print(f'incorrect pin and you have only {remain_A}')
            else:
                print('card is block')
                break
    else:
        print('Please enter only 4 digit atm pin')
