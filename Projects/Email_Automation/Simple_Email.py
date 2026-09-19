""" Python --> Automation --> Email Automation --> Google Mail

Simple Mail Automation
Mail OTP
Mail With Subject & Attachements
Bulk Mail"""

"""
#jrva twgm gmlr olqz--password

#Simple Mail Automation--SMTP
import smtplib
#First lets make server connection #Port Address and host
server=smtplib.SMTP('smtp.gmail.com',587)
#print(server)
#start the connection
server.starttls()
#login
server.login("anupojumeghana07@gmail.com","jrva twgm gmlr olqz")
msg="Hello this is Megha,Hope you are doing well and improving daily"
server.sendmail("anupojumeghana07@gmail.com","gurubillidurga@gmail.com",msg)
#close the connection
server.quit()
print("mail sent") """

"""#Now lets send OTP to mail and validate the script

import math
import random
import smtplib
a=random.randint(1000,9999)
msg=(f'Your otp is {OTP}')
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
#login
server.login("anupojumeghana07@gmail.com","jrva twgm gmlr olqz")
server.sendmail("anupojumeghana07@gmail.com",a)
otp=int(input())
if otp==a:
    print("Granted")
else:
    print("Wrong")
server.quit()
print("Mail sent")"""

"""
import math
import random
import smtplib
#In the case i will use math and random modules together
digits='1234567890'
OTP=""
for i in range(6):
    OTP+=digits[math.floor(random.random()*10)]
    #print(OTP)
msg=(f'Your otp is {OTP}')
server=smtplib.SMTP('smtp.gmail.com',587)
#print(server)
#start the connection
server.starttls()
#login
server.login("anupojumeghana07@gmail.com","jrva twgm gmlr olqz")
server.sendmail("anupojumeghana07@gmail.com","anupojumeghana09@gmail.com",msg)
#print("mail sent")
a=input("Enter the number")
if a==OTP:
    print("Access Granted")
else:
    print("Wrong")
#close the connection
server.quit()
print("Mail sent") """

""" In this case we need to add subject and to address for mail we will use package"""

#Multipurpose Mail Extension
import email
import smtplib
#MIME --> Multipurpose Interner Mail Extention
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText
#now we will provide the details
From="anupojumeghana07@gmail.com"
To="gurubillidurga@gmail.com"
Subject="Python Full Stack"
#Now we will check all the details and throw it to Multipart
msg=MIMEMultipart()
print(msg)
print(type(msg))
msg['From']=From
msg['To']=To
msg['Subject']=Subject
msg['body']="Hey guys,what's the learning plan for this week"
msg.attach(MIMEText(msg['body'],'plain'))
text=msg.as_string()
server=smtplib.SMTP('smtp.gmail.com',587)
#print(server)
#start the connection
server.starttls()
#login
server.login("anupojumeghana07@gmail.com","jrva twgm gmlr olqz")
server.sendmail(From,To,text)
#close the connection
server.quit()
print("mail sent")











