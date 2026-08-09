""" --> This module is used to send a mail without using mail or outlook by running the python code
    --> Here by using port (587) """


import smtplib
sender_email='anupojumeghana07@gmail.com'
sender_app_password='qglu xdoi lgke mule'
receiver_email=['yaminibadithaboyina@gmail.com','anupojumeghana09@gmail.com']

message="""

Hello,

This mail was sent using python

Regards
Python Team """


server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender_email,sender_app_password)
server.sendmail(sender_email,receiver_email,message)

server.quit()
print('Email sent successfully') 

""" E-mail with subject """

import smtplib
from email.message import EmailMessage

msg=EmailMessage()
sender_email='anupojumeghana07@gmail.com'
sender_app_password='qglu xdoi lgke mule'
receiver_email='anupojumeghana09@gmail.com'

msg['from']=sender_email
msg['to']=receiver_email
msg['Subject']='Python Mail'

msg.set_content("""

Hello,

This mail was sent using python

Regards
Python Team
""")

server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender_email,sender_app_password)
server.send_message(msg)
server.quit()
print('Email sent successfully') 


""" Email importing with file,for sending more than 1 people use list [email 1 ,email 2..etc]"""

import smtplib
from email.message import EmailMessage

msg=EmailMessage()
sender_email='anupojumeghana07@gmail.com'
sender_app_password='qglu xdoi lgke mule'
receiver_email='anupojumeghana09@gmail.com'

msg['from']=sender_email
msg['to']=receiver_email
msg['Subject']='Python Mail'

msg.set_content("""

Hello,

This mail was sent using python

Regards
Python Team
""")

with open('set.py','rb') as file:
    file_content=file.read()
    msg.add_attachment(file_content,maintype='application',subtype='py',filename='set.py')

server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender_email,sender_app_password)
server.send_message(msg)
server.quit()
print('Email sent successfully')

