"""
Inheritence :

--> Inheritence is the process of inherite one class into another class
--> Will generally inhertie from a class is called parent class and using it in another that class is called child class """


class company:  
    def salary(self): 
        print("Company Salary")

class employee(company):
    def mon_sal(self):
        print("Employee Salary ")

per_sal=employee()
per_sal.mon_sal()
per_sal.salary()

"""Types of Inheritence :

1.Single Inheritence
2.Multiple Inheritence
3.Multi-Level Inheritence
4.Hierarchical Inheritence
5.Hybrid Inheritence

1.Single Inheritence :

--> If one child class inherit from one parent class this is called single inheritence """ 

class father:
    def land(self):
        print("5 acer land")
        
class me(father):
    def flat(self):
        print("6 flates")
all_=me()
all_.flat()
all_.land()

"""2.Multiple Inheritence :

--> If one child inherit from more than one parent class this is called Multiple Inheritence """

class father:
    def home(self):
        print('Home at village')
        
class mother:
    def gold(self):
        print('50 KG gold')
        
class dau(father,mother):
    def flat(self):
        print('Flat')
all_to=dau()
all_to.home()
all_to.gold()
all_to.flat()

"""3.Multi-Level Inheritence :

--> One child class become parent class to the another class is called multi-level inheritence """

class grandfather:
    def land(self):
        print("G Land")

class father(grandfather):
    def flat(self):
        print("Flat")

class dau(father):
    def car(self):
        print("Car")
fam=dau()
fam.land()
fam.flat()
fam.car()

"""4.Hierarchical Inheritence :

-->If two child class inheritence from one parent is called as hierarchical """ 

class father:
    def land(self):
        print("50 acher land")

class son(father):
    def flat(self):
        print("Flat")

class dau(father):
    def car(self):
        print("Car")

s=son()
s.land()
s.flat()

d=dau()
d.land()
d.car()

"""5.Hybrid Inheritence:

--> Inheritence more than two types into one class is called Hybrid Inheritence  """

class person:
    def name(self):
        print('Megha')

class student(person):
    def study(self):
        print('B Tech Final year')

class py_teacher:
    def teach(self):
        print('Python')

class java_teacher:
    def teac(self):
        print('Java')

class learner(py_teacher,java_teacher):
    def learn(self):
        print('Learner')

class all_get(student,learner):
    def get_it(self):
        print("This Persons getting all data")

an=all_get()
an.name()
an.study()
an.teach()
an.teac()
an.learn()
an.get_it()


"""---Single Inheritence Example """

class animal:
    def type(self):
        print("Animal")

class dog(animal):
    def walk(self):
        print("Dogs")

an=dog()
an.type()
an.walk()

"""--Multiple Inheritence Example---- """

class dog:
    def type(self):
        print("Dog")

class cat:
    def typ(self):
        print("Cat")

class animals(dog,cat):
    def ani(self):
        print("Animals")

an=animals()
an.type()
an.typ()
an.ani()

"""----Multi-Level Example -----"""

class college:
    def clg(self):
        print("VIEW")

class Branch(college):
    def br(self):
        print("ECE")

class Section(Branch):
    def sec(self):
        print("A")

ex=Section()
ex.clg()
ex.br()
ex.sec()

"""---Hierarchical Inheritence Example------"""

class color:
    def co(self):
        print("Color")

class Blue(color):
    def blue_1(self):
        print("Blue")

class Black(color):
    def black_1(self):
        print("Black")

c1=Blue()
c1.co()
c1.blue_1()

c2=Black()
c2.co()
c2.black_1()

"""-----------------Hybrid Inheritence Example------------ """

class College:
    def clg(self):
        print("VIEW")

class Branch(College):
    def bran(self):
        print("ECE")

class python:
    def py(self):
        print("Python")

class java:
    def ja(self):
        print("Java")

class subject(Branch,python,java,):
    def sub(self):
        print("Learn")

su=subject()
su.clg()
su.bran()
su.py()
su.ja()
su.sub() 
 

     





    
        






        
































        
