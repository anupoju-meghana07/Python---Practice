""" Matplotlib

--> This is an python library used to create graphs and chats
 Plot:
--> The function can create a line graphs with given data
 xlabel:
--> Used to represent the x-axis values
 ylabel:
--> Used to represent the y-axis values
 title:
--> To define the title of the graph 

--> Line Graph"""

import matplotlib.pyplot as plt
marks=[45,48,90,95]
stu=['Megha','Durga','yamini','Lalli']
plt.plot(stu,marks,color='blue')
plt.title('Student_Marks')
plt.xlabel('Students')
plt.ylabel('Marks')
plt.show()

"""--> Bar Graph """

import matplotlib.pyplot as plt
sales=[890,150,800,1200]
cars=['BMW','Nano','Swipf','Toyoto']
plt.bar(cars,sales,color='purple')
plt.title('Car_sales')
plt.xlabel('Company names')
plt.ylabel('Number of Sales')
plt.show()

"""--> Bar Graph Horizontal """

import matplotlib.pyplot as plt
sales=[890,150,800,1200]
cars=['BMW','Nano','Swipf','Toyoto']
plt.barh(cars,sales,color='violet')
plt.title('Car_sales')
plt.ylabel('Company names')
plt.xlabel('Number of Sales')
plt.show()

"""--> Pie Chart: """

import matplotlib.pyplot as plt
subjects=['Python','Java','C']
students=[45,26,39]
plt.pie(students,labels=subjects)
plt.title('Total Students')
plt.legend(subjects)
plt.show()

"""--> Scatter Chart """

import matplotlib.pyplot as plt
stu=['Megha','Durga','Lalli','Yamini']
marks=[55,56,70,90]
plt.scatter(stu,marks)
plt.title('Student_Marks')
plt.xlabel('Students')
plt.ylabel('Marks')
plt.show()

"""--> Histography """

import matplotlib.pyplot as plt
sales=[890,150,800,1200]
plt.hist(sales)
plt.title('Sales_hist')
plt.xlabel('Sales')
plt.ylabel('Frequency')
plt.show()

"""--> Box Plot """

import matplotlib.pyplot as plt
marks=[40,50,60,70,80,90]
plt.boxplot(marks)
plt.show()


















































