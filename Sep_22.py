"""Usage of super()
#Super with arguments --> super().__init__(args) 

class Father:
    Father class with fproperty amount 
    def __init__(self,fproperty):
        self.fproperty=fproperty
    def father_property(self):
        print(f'Father Property is {self.fproperty}')
class kid(Father):
    Kid class with kproperty argument
    def __init__(self,kproperty,fproperty):
        super().__init__(fproperty)
        self.kproperty=kproperty
    def kid_property(self):
        print(f'Kid Property is {self.kproperty}')
        print(f'Total combined property is {self.fproperty + self.kproperty}')
u1=kid(500000,250000)
u1.kid_property()     #Attribute Error
u1.father_property()
print(u1.__dict__)  

#Cal the areas of square,rectangle

class Square:
    Area of Square
    def __init__(self,x):
        self.x=x
    def area(self):
        print(f'Area of square is  {self.x*self.x}')
class Rectangle(Square):
    Derived Class
    def __init__(self,x,y):
        self.y=y
        super().__init__(x) #Calling superclass constructor with args 
    def area(self):
        #super().area() #Calling superclass with method it will give square first
        print(f'Area of Rectangle is {self.x * self.y}')
        super().area()
obj1=Rectangle(10,8)
obj1.area()
x,y=map(int,input("Enter the values").split(',')) #Accepting mul values from users
obj2=Rectangle(x,y)
obj2.area()

#obj2=Square(5) #As we are creating diff objects its possible
#print(obj2.area())  

#Multiple Inheritence --> Whatsapp Scenario -->Users,Business Users,Premium Users

Multiple base classes with single derived class

class base1:
    statement(s)........
    .........
class base2:
    statement(s)........
    .........
class derived(base1,base2):
    statement(s)........
    .........
    
class users:
    Users class with basic features
    def voice_call(self):
        print("User can make voice calls")
class Notifications:
    Notifications reaching out
    def send_notification(self):
        print("User can get pop-up notifications")
class PremiumUsers(users,Notifications):
    Extra Features added
    def verification_badge(self):
        print("User is verified and bluetick added")
u1=PremiumUsers()
u1.verification_badge()
u1.voice_call()
print(dir(u1))

Multilevel  Inheritence --> Level by level

class base1:
    statement(s)....
    .........
class base2(base1):
    statement(s)....
    .........
class base3(base2):
    statement(s)....
    .........

class Users:
    Users class with base function
    def send_messages(self):
        print("Users can send messages")
    def voice_call(self):
        print("Making voice call")
class BussinessUsers(Users):
    First Derived Class
    def create_catalog(self):
        print("Details added successfully")
class PremiumUsers(BussinessUsers):
    Second Derived Class
    def verification_badge(self):
        print("Account is verified")
u1=PremiumUsers()
u1.verification_badge()
u1.create_catalog()
u1.send_messages()
u1.voice_call()

Hierarchy Inheritence
class base1:
    statement(s)....
    .........
class base2(base1):
    statement(s)....
    .........
class base3(base1):
    statement(s)....
    .........  

class users:
    using Hierarchy Inheritence
    def send_messages(self):
        print("You can send messages")
class Notification(users):
    Derived class
    def send_notification(self):
        print("Users can get notifications")
class Subcription(users):
    Second derived class
    def sub_not(self):
        print("Users can Subscribe")
u1=Subcription()
u1.sub_not()
u1.send_messages() """

# Using super

class Users:
    """Using Hierarchical Inheritance"""
    def __init__(self, msgs):
        self.msgs = msgs
        print("You can send messages")
class Notification(Users):
    """First Derived Class"""
    def __init__(self, msgs, notifi):
        self.notifi = notifi
        super().__init__(msgs)
        print("Users can get notifications")
class Subscription(Users):
    """Second Derived Class"""
    def __init__(self, msgs, sub):
        self.sub = sub
        super().__init__(msgs)
        print("Users can Subscribe")

u1 = Subscription("Hello", "YouTube")
print(u1.msgs)
print(u1.sub)


    
 




    
