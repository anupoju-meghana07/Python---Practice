#Every Python file--> Module --> import keyword

"""import Sep_10
print(dir(Sep_10)) #dir--> Directory will return all available methods,attributes
print(type(Sep_10.employees))
print(type(Sep_10.details))

Sep_10.employees("Megha",desgination="Trainee",location="Vizag")
#print(Sep_10.details.keys())
print(Sep_10.details['Organization'])
#Update dict
Sep_10.details.update({'batches':['PFS','JFS','DA','AAA','DS'],'employees':240})
print(Sep_10.details) 

#from keyword

from Sep_10 import employees,details
details.update({'batches':['PFS','JFS','DA','AAA','DS'],'employees':240})
#print(details)
print(Sep_10.__doc__) """  #Returns  Doc String from the given module


#Built-in-modules --> math,random,os,time,datetim

#Build a QR CODE SCANNER USING Python --> Linkedin URL
#pyqrcode,png
#pip install pyqrcode
#pip install pypng

import pyqrcode
import png

#Create a QRCode by giving a link

link="https://www.linkedin.com/in/meghana-anupoju-460952288"
qr=pyqrcode.create(link)
#print(qr)
qr.png("myqr.png",scale=10)





