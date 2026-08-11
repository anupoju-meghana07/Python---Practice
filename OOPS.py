"""
OOPs:

--> object oriented programming system
--> OOps is used to maintain the code structure in object and classes

1 class
2 object
3 attribute
4 methods

1.class :

-->Class is a blueprint or template to an  object
-->Syntax: class(keyword) Name:
                #attributes
                #methods

2.object:

--> Obj is instance of the class
--> Syntax:class(keyword) Nmae:
            #attributes
            #methods
          any_=class_name """

class person:
    name='Megha'
    Edu='B.Tech'
p1=person()
print(p1.name)
print(p1.Edu) 

class codegnan:
    city='Vizag'
    Tech='Python'
    data='MySql' #class Atrributes
code=codegnan()
print(code.city)

"""3.Attributes:

--> Attributes is the data present in the class or pass to the class

ex: Take car
-------------------
      Color
      Brand
      Seat  """

class Megha:
    name='Anupoju'
    age=22
    B_G='B.Tech'
an=Megha()
print(an.name) 

class car:
    def __init__(self):
        self.color='Black'
        self.seat=6
        self.brand='BMW'
c1=car()
print(c1.color)
print(c1.seat)
print(c1.brand)

class details:
    def __init__(self):
        self.name='Megha'
        self.age=21
        self.B_G='B-Tech'
        self.role='Student'
person=details()
print(person.name)
print(person.age)
print(person.B_G)
print(person.role) 

class bank:
    def __init__(self):
        self.name='Megha'
        self.adhaar=689934667
        self.pan='A56Z79636'
        self.ph_no=5897934378
details=bank()
print(details.name)
print(details.adhaar)
print(details.pan)
print(details.ph_no)

"""4.Methods

--> Method is a function that is created inside the class
--> Syntax: class(keyword) name:
                #attributes
                def func_name(self):
                    #code
            obj=class_name()
            print(obj.func_name()) """

class student:
    def __init__(self):
        self.name='Megha'
        self.age=21
        self.course='PFS'
        
    def st_name(self):
        print(self.name)
        print(self.age)
        print(self.course)

    def all_data(self):
        print(self.name)
        print(self.age)

stu_=student()
stu_.st_name()
stu_.all_data() 

class car:
    def __init__(self):
        self.color='Blue'
        self.seat=6
        self.Brand='BMW'
        
    def brake_(self):
        print(f'{self.Brand} brake will apply at speed 250KM')

    def accelator_(self):
        print(f'{self.Brand} will take 2 sec to reach 180 speed')

    def clucth(self):
        print(f'{self.Brand} with {self.seat} is automatic')

car_=car()
car_.brake_()
car_.accelator_()
car_.clucth()      

class student:
    def __init__(self,name,age,batch):
        self.name=name
        self.age=age
        self.batch=batch

    def all_data(self):
        print(self.name)
        print(self.age)
        print(self.batch)
        
stu_1=student('Megha',21,5)
stu_1.all_data()

stu_2=student('Durga',21,5)
stu_2.all_data()                 

class bank:
    
    def __init__(self,name,adhaar,pan):
        self.name=name
        self.adhaar=adhaar
        self.pan=pan

    def all_data(self):
        print(self.name)
        print(self.adhaar)
        print(self.pan)

user_1=bank('Megha',6893553487,'A57A89R55')
user_1.all_data()

user_2=bank('Durga',657893789,'M47FSS679')
user_2.all_data()


    
        
        
        
















            
            

    












    





















