"""
--> Abstraction means hiding the implemented data and showing only need data to user
-->ABC : Abstract Base class
--> The abstract method is used to hide that paticular information of a base class 

from abc import ABC,abstractmethod
class gov_bank(ABC):
    @abstractmethod
    def interest(self):
        print('Government interest is 3.5')
        
class SBI_bank(gov_bank):
    def interest(self):
        print('SBI bank interest is 7.8')

class ICIC_bank(gov_bank):
    def interest(self):
        print('ICIC bank interest is 8.9')

obj=SBI_bank()
obj.interest()

obje=ICIC_bank()
obje.interest() 


from abc import ABC,abstractmethod
class clg_fee(ABC):
    @abstractmethod
    def fee_str(self):
        print('College fee 45000')

class mang(clg_fee):
    def fee_str(self):
        print('College fee 100000')

class EM(clg_fee):
    def fee_str(self):
        print('College fee 15000')

obj=mang()
obj.fee_str()

gov=EM()
gov.fee_str()

--> Create a class Vechile child class like bike or car 

class Vechile:
    def ve(self):
        print("Vechiles")

class Bike(Vechile):
    def bi(self):
        print("Bikes")

class Car(Vechile):
    def cr(self):
        print("Cars")

obj=Bike()
obj.ve()
obj.bi()


obj_1=Car()
obj_1.ve()
obj_1.cr() """

"""--> Create a cal using add methods it should display the arguments """

class cal:
    def add_(self,a,b,c=0,d=0):
        return a+b+c+d
obj=cal()
print(obj.add_(7,8))
    

        
