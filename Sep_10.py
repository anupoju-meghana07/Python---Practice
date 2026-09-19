"""
Scenario to Understand (*args and **kwargs) 

#Employee Details """

def employees (*names,**settings):
    """Employee Detail along with their settings"""
    print("Employee Names")
    for employee in names:
        print('---------')
        print('-',employee)
    for key,value in settings.items():
        print("Key is", key)
        print("Value is",value)
employees("Rahul","Akash","Saritha",department="Operations",experience_letters=True,salary=True)

#Shopping Details

def shopping(*product,**filters):
    """Shopping Detail with filters """
    print("Shopping Details")
    for name in product:
        print(name)
    for key,value in filters.items():
        print(f"{key} : {value}")
shopping("Laptop","Mouse","Buds",price=19000,colour="Blue",rattings=4)

"""

#Module: A module is simple python file (reusable,organized code)

import --> keyword

Employee Details/Performance metrics(employee.py)
  -->employee func
  -->performance func
  -->Metric            """

def employees (*names,**settings):
    """Employee Detail along with their settings"""
    print("Employee Names")
    for employee in names:
        print('---------')
        print('-',employee)
    for key,value in settings.items():
        print("Key is", key)
        print("Value is",value)
employees("Rahul","Akash","Saritha",department="Operations",experience_letters=True,salary=True)

#if __name__ == "__main__":
details={'Organization':'Codegnan','Year':2018,'branches':['Vijayawada','Hyderabad','Vizag']}
print(__name__)      #Dunder Methods --> Magic Methods




