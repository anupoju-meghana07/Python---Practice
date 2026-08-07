"""--> Exception Handling

-->Error can be handled by try and except

1.try:

--> We can write code here which may contain any error """

try:
    print(n)
except:
    print("Some Error ")
    
""" 2.except:

--> Exception can handle any error that come in the try block

Examples:"""

try:
    num=0
    num_2=8
    print(num_2/num)
except:
    print("Zero Division Error")

try:
    any_=int(input("Enter any number : "))
    print(any_+9)
except:
    print("Error")

try:
    print(9+'python')
except:
    print('Error')

""" 3.else:

--> If no error in the code were raised,then the else block will execute

Examples: """

try:
    print(9+7)
except:
    print('Error')
else:
    print('No error')

try:
    print(9/0)
except ZeroDivisionError:
    print('This will rise zero division error')
else:
    print('No error')

try:
    print(9/0)
    print(num)
except ZeroDivisionError:
    print('This will rise zero division error')
except NameError:
    print('This will rise NameError')    
else:
    print('No error')

try:
    print(9+'Python')
    print(9/0)
    print(num)
except ZeroDivisionError:
    print('This will rise zero division error')
except NameError:
    print('This will rise NameError')
except TypeError:
    print('This will rise TypeError')
else:
    print('No error')    


""" 
4.finally:

--> This block will execute if the present in the try block or not """

try:
    print ('Hello')
except ZeroDivisionError:
    print('This will rise zero division error')
except NameError:
    print('This will rise NameError')
except TypeError:
    print('This will rise TypeError')
else:
    print('No error')
finally:
    print('End')


"""----------------------------------------  File Handling -------------------------------

--> An file handler is an object used to connect with that particular file

1. with(keyword)

--> By using with keyword no need to close the file,it will close it by itself

Syntax:

with open('file_name','mode') as name
with open(r'file_path','mode') as name

Example: """

with open('demo.txt','r') as file_:
    print(file_.read())

"""2.Open() :

-->By using this we have to close the file by using close()

Example: """

any_=open('demo.txt','r')
print(any_.read())
any_.close()

"""--> Modes

1.'r'

The 'r' mode is used for functions read(),readline() and readlines()

Ex: """

with open('demo.txt','r') as file_:
    print(file_.read())

"""2.'w'

--> The write mode is used for write() func
Ex: """

with open('demo.txt','w') as file:
    file.write('Time') 
    
"""3.'a':append

--> The 'a' mode is used for write() func and it will add the text at last position

Ex: """

with open('demo.txt','a') as file:
    file.write('Python')


"""4.'x':Create file """

with open('megha.txt','x') as file:
    file.write('Python module take 2 hrs per day')

"""
--> Function :

1.write() :
2.read():
-->It will read() func will read the file chunk by chunk where we can specify the size """

with open('demo.txt','r') as file:
    print(file.read(5))

"""3.readline():

--> It will only read one line at a time """

with open('demo.txt','r') as file:
    print(file.readline())
    
"""4.readlines():

-->The readlines() will read whole file and written it in a list where each line is one index in the list """

with open('demo.txt','r') as file:
    print(file.readlines())

    











    
    
