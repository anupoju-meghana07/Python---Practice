""" OOP ---> Object Oriented Programming --> Objects

#Chair(object)-->Wood(Material),Design(Dimensions),Person

--> A class is a blueprint of a object
-->A object is a real word entity which contains --> Attributes(variables) ,Methods(Functions)

class keyword

Flipkart-->Products-->laptop,mobiles,gadgets...
Features-->Encapsulation,Inheritence,Polymorphism

class ClassName:
    """docstring""" #description
     #attributes (define the data)
     .....
     .....
     def fname(self): #behaviour
     def __init__(self):
         statement(s)...
         .........
obj=ClassName() 

#Students -->name,age
#self:Current instance 

class Students:
    """Student Details"""
    name="Akash"  #class attributes
    age=22
    place="vizag"

    def details(self): #methods
        print(f'{self.name} is in {self.place} and age of {self.age} years')

#creation of objects
st1=Students()
print(st1)
print(dir(st1))
print(st1.name,st1.age,st1.place)
#print(st1.details()) #TypeError
#print(st1.details()) #NameError as we have thrown self but no reference
#now we pass the reference
st1.details()
st2.details() #In above case how many ojects you create the result will be same 

class Students:
    """Student details for multiple students"""
    def details(self,name,age,place):
        self.name=name  #to make it dynamic
        self.age=age
        self.place=place
    #Now to access those details
    def display(self):
        print(f'Student name is {self.name}')
        print(f'Student age is {self.age} and lives in {self.place}')

st1=Students()
st1.details("Megha",22,"Vizag")
print(st1.name,st1.place)
st1.display()
print(st1.__class__)
print(st1.__doc__)
print(st1.__dict__)   #{'name': 'Megha', 'age': 22, 'place': 'Vizag'}
st2=Students()
st2.details("Durga",22,"Vizag")
st2.display()
print(st2.__dict__)  

#Object to be initialized directly --> __init__()

class Students:
    """Student details for multiple students""" 
    def __init__(self,name,age,place):   
        self.name=name  #instance variables
        self.age=age
        self.place=place
    #Now to access those details
    def display(self):   #instance methods
        print(f'Student name is {self.name}')
        print(f'Student age is {self.age} and lives in {self.place}')
st1=Students("Vivek",22,"Hyd")
st1.display()
st2=Students("Yamini",23,"hyd")
st2.display()
print(st2.__dict__)  

#Create a Cars class with attributes as brand,name,price
#Create mul objects

class Cars:
    """Details of Cars using multiple objects""" 
    def __init__(self,brand,price,colour):
        self.brand=brand
        self.price=price
        self.colour=colour
    #To access those details
    def show(self):
        print(f'The brand of car is {self.brand} and ptice is {self.price}')
car1=Cars("BMW",2000000,"Black")
car1.show()
car2=Cars("Nexson",100000,"White")
car2.show()  

#Encapsulation --> How that methods and attributes are binded to single
#class, in similar way how we can access the data -->Public,Protected,Private

#Public : Created and modified even outside the class

class Users:
    """Usage of Public attributes"""
    def __init__(self,username):
        self.user=username #Public Attribute
    def display(self):
        print(f'Username is {self.user}')  #display : method , #username:Attributes

u1=Users("TOM")
print(u1.user)
u1.user="Sam"  #We can modify the public Attribute
print(u1.user)
u1.display()  

#Protected Attribute --> These can also be modified outside the class,its mainly useful as a hint/coding convention for other users/developers
#To create a protected attribute we use underscore --> _otp

class Users:
    """Usage of Public attributes"""
    def __init__(self,username,_otp):
        self.user=username #Public Attribute
        self._otp = _otp   #Protected Attribute
    def display(self):
        print(f'Username is {self.user}')
        print(f'OTP is {self._otp}')
u1=Users("Saketh",7891)
u1.display()
u1._otp=9081
u1.display() 

#Private Attribute --> Restrict The usage and cannot be directly accessed
#We have the usage or notation as double leading underscore --> __password


class Users:
    """Usage of Private attributes""" 
    def __init__(self,username,_otp,__password):
        self.user=username          #Public Attribute
        self._otp = _otp            #Protected Attribute
        self.__password=__password  #Private Attribue
    def display(self):
        print(f'Username is {self.user}')
        print(f'OTP is {self._otp}')

u1=Users("Vijay",5347,"admin123")
print(u1.user,u1._otp)
#print(u1.__password)  AttributeError
print(u1.__dict__)
#In above case password can't be accessed directly --> NameMangling -- Accessing through class
print(u1._Users__password) """

#Usage of getter(),setter() Methods  

class Users:
    """Usage of Private attributes """
    def __init__(self,username,_otp,__password):
        self.user=username          #Public Attribute
        self._otp = _otp            #Protected Attribute
        self.__password=__password  #Private Attribute
    #Usage of getter() or get() method for password
    def get_password(self):
        """Getter method for password"""
        #return "******"               #It will return only in *
        return self.__password         #To see password
    #Usage of setter() to modify the data
    def set_password(self,new_password):
        if len(new_password)<6:
            return 'Password length is not matching'
        else:
            self.__password=new_password
            return 'Updated Password'
u1=Users("Admin",4567,"orange")
print(u1.get_password())
print(u1.set_password("admin")) #Not Satisify the requirement less than 6
print(u1.set_password("admin123")) #Case satisified
print(u1.get_password())
print(u1.__dict__)

    
















