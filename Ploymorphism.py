"""
super():

--> This super method is used to get the constructor from the parent class and use in the child class
-->And also we can get any method from the class """

class person:
    def __init__(self,name,age,role):
        self.name=name
        self.age=age
        self.role=role
        
class employee(person):
    def __init__(self,name,age,salary,role):
        super(). __init__(name,age,role)
        self.salary=salary

obj = employee('Megha',21,100,"Python Developer")
print(obj.name)
print(obj.age)
print(obj.salary)
print(obj.role)  

class all_:
    def job_(self):
        print("Looking for job")

class Looking(all_):
    def job_in(self):
        print("Looking for candidates")

    def an_(self):
        super().job_()
        print("No Jobs")
        
any_=Looking()
any_.an_()

"""----------------------Ploymorphism---------------

--> Ploymorphism means a same name but different forms

1.Method Overloading
2.Method Overriding
3.Operation Overloading

1.Method Overloading :

--> This happens in a class if same name of method is created,but the recent method will be activated before one will not be considered """

class data_:
    def add_(self,a,b):
        return a+b
    def add_(self,a,b,c):
        return a+b+c
    def add_(self,a,b,c,d):
        return a+b+c+d
obj=data_()
print(obj.add_(7,8,9,10))

"""2.Method Overriding :

--> This method overriding happens when a parent class and child class have same method and the child class takes its own implementation """ 

class pay:
    def payment(self):
        print('Payment called')

class UPI(pay):
    def payment(self):
        print("UPI payment called")

class Paytm(pay):
    def payment(self):
        print("Paytm is called")

obj=UPI()
obj.payment()

get=Paytm()
get.payment()

"""3.Operation Overloading:

--> Which gives the special meaning to the operator when it is called by object

1.__add__ : +
2.__sub__ : -
3.__mul__ : *
4.__truediv__ :/

1.__add__ : + """

class cal:
    def __add__(self,a,b):
        print(a+b)

how=cal()
how.__add__(7,8) 

class cal:
    def __init__(self,any_):
        self.any_=any_
    def __add__(self,do):
        print(self.any_+do.any_)

how=cal(7)
who=cal(8)
how.__add__(who) 

class cal:
    def __init__(self,any_):
        self.any_=any_
    def __add__(self,do):
        print(self.any_+do.any_)

how=cal(7)
who=cal(8)
print(how+who)

"""2.__sub__ : - """

class cal:
    def __init__(self,any_):
        self.any_=any_
    def __sub__(self,do):
        print(self.any_-do.any_)

how=cal(8)
who=cal(7)
print(how-who)

"""3.__mul__ : *"""

class cal:
    def __init__(self,any_):
        self.any_=any_
    def __mul__(self,do):
        print(self.any_*do.any_)

how=cal(8)
who=cal(7)
print(how*who)

"""4.__truediv__ : / """

class cal:
    def __init__(self,any_):
        self.any_=any_
    def __truediv__(self,do):
        print(self.any_/do.any_)

how=cal(8)
who=cal(7)
print(how/who)












    


        
