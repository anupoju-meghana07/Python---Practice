""" --- Constructor ----

--> __init__ :

--> The constructor is a spl method that only run when the object is created
-->Mostly we will take data inside this method  """

class cls_data:
    def __init__(self):
        self.name='Megha'
        self.Course='Python'
cls=cls_data()
print(cls.name)
print(cls.Course)

"""--> self :

--> The self keyword reffers to the current object """

class stu:
    def __init__(self):
        self.name='Megha'

    def any_(self):
        print(self.name)

s1=stu()
s1.any_() 

class stu_data:
    def __init__(self,name,batch,age):
        self.name=name
        self.batch=batch
        self.age=age
        
    def student(self):
        print(f'{self.name} from batch {self.batch} and age {self.age}')

data1=stu_data('Megha',5,21)
data1.student()

"""------------Encapsulation----------

--> Wrapping data and methods together is called as encapsulation and using or controlling the data in methods """

class stu_data:
    def __init__(self,name,batch,age):
        self.name=name
        self.batch=batch
        self.age=age
        
    def student(self):
        print(f'{self.name} from batch {self.batch} and age {self.age}')

data1=stu_data('Megha',5,21)
data1.student()

"""---Access Specifiers --

1 Public(name):

-->This can be accessed normally and call it like a normal variable
Ex : 

self.name=name
print(self.name) """

"""2 Protected (_name) :

--> Just by adding single underscore (_) before a variable it becomes protected variable

Ex : 

self._age=age
print(self._age) """


class stu_data:
    def __init__(self,name,batch,age,fee):
        self._name=name
        self._batch=batch
        self._age=age
        self._fee=fee
        
    def only_name(self):
        print(f'{self._name}')

    def only_batch(self):
        print(f'{self._batch}')

    def only_age(self):
        print(f'{self._age}')

    def only_fee(self):
        print(f'{self._fee}')

data1=stu_data('Megha',5,21,450000)
data1.only_name()
data1.only_batch()
data1.only_age()
data1.only_fee()

"""3 Private (__name)

--> Adding (__) before a variable it becomes private variable

ex : 

self.__balance=balance
print(self.__balance)  """


class bank_ac:
    def __init__(self):
        self.name='Megha'
        self.Adr='5673799378'
        self.pan='72M67V79034'
        self.__balanace=4500

    def details(self):
        print(self.name)
        print(self.Adr)
        print(self.pan)
    def bank_bal(self):
        print(self.__balance)

acc=bank_ac()
acc.details() 

class employee:
    def __init__(self):
        self.name='Megha'
        self.role='Python Developers'
        self.__salary=82000
        self._experience=4.5
        self._emptype='Full-Time'
        
    def details(self):
        print(self.name)
        print(self.role)

    def income_(self):
        print(self.__salary)

    def type_(self):
        print(self._experience)
        print(self._emptype)

emp=employee()
emp.details()
emp.income_()
emp.type_()     

class university:
    def __init__(self):
        self.name='Megha'
        self.course='ECE'
        self.sec='A'
        self.__marks=90
        self._fees=80000

    def details(self):
        print(self.name)
        print(self.course)
        print(self.sec)

    def pri_(self):
        print(self.__marks)

    def pro_(self):
        print(self._fees)

uni=university()
uni.details()
uni.pri_()
uni.pro_()
        
        
        
        

        
        
        
        



























