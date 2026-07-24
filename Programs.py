"""
--> Even or Odd upto certain range"""

limit_=int(input('Enter the limit:'))
for j in range(1,limit_+1):
    if j%2==0:
        print(f'{j} is even')
    else:
        print(f'{j} is odd')

"""--> Prime no or not"""

num=int(input('Enter a num : '))
count=0
for j in range(1,num+1):
    if num%j==0:
        count+=1
if count==2:
    print(f'{num} is prime')
else:
    print(f'{num} is not prime')

"""--> Prime or Not (Inner loops)"""

for i in range(2,10):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if count==2:
        print(f'{i} is prime') 

"""---> String Reverse"""
rev_=input('Enter Name:')
emp_=''
for j in rev_:
    emp_=j+emp_
if emp_==rev_:
    print(f'{rev_} is a palindrome')
else:
    print(f'{rev_} is not a palindrome')
"""
-->*
   **
   ***
   **** """          
start_=int(input("Enter a num:"))
for j in range(1,start_+1):
    for i in range(1,j+1):
        print('*',end='')
    print()
"""    
--> 1
    12
    123
    1234 """          
start_=int(input('Enter the num:'))
for j in range(1,start_+1):
    for i in range(1,j+1):
        print(i,end='')
    print()
          
"""
--> 1
    2 3
    4 5 6
    7 8 9 10  """

count=0
start_=int(input('Enter the num:'))
for j in range(1,start_+1):
    for i in range(1,j+1):
        count+=1
        print(count,end='')
    print()
"""
-->Reverse traingle(Numbers)
     1234
     567
     89
     10 """

count=0
start_=int(input('Enter the num:'))
for j in range(start_,0,-1):
    for i in range(1,j+1):
        count+=1
        print(count,end='')
    print()
    
"""--> Reverse of Stars
*****
****
***
**
*  """

start_=int(input("Enter a num:"))
for j in range(start_+1,0,-1):
    for i in range(1,j+1):
        print('*',end='')
    print()
"""
-->   * 
     * * 
    * * * 
   * * * * 
  * * * * * 
 * * * * * * 
* * * * * * * (pyramid)"""


num=7
for j in range(num):
    print(" " *(num -j -1),end = '')
    print('* ' * (j+1))


"""    
* * * * * * * 
 * * * * * * 
  * * * * * 
   * * * * 
    * * * 
     * * 
      * (Reverse Pyramid)"""

num=7
for j in range(num,0,-1):
    print(" " *(num - j),end = '')
    print('* ' * j)

"""--> Removing the duplicates from the list"""

nums=[1,2,2,5,5]
emt_=[]
for j in nums:
    if j not in emt_:
        emt_.append(j)
print(emt_)

"""--> Perfect Number"""

num=int(input('Enter a num:'))
per_num=0
for j in range(1,num):
    if num%j==0:
        per_num+=j
if per_num==num:
    print(f'{num} is perfect num')
else:
    print(f'{num} is not a Perfect num')
    

    



   


    


        
       
   
        


        
