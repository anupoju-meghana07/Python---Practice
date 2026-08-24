'''
pandas
------
-->pandas are python library used analysis and manipulation on structure data such as table, csv file
--> to use pandas need to import
eg-- '''

import pandas as pd
data_=pd.Series([1,2,3,4,5,6])
print(data_)

'''functions
---------
1.Series
--------
--> This function is a one-dimenstions labeled data structure
--> The right is the index values which starts from 0
--> and the other side are normal values
eg--'''

import pandas as pd
data_=pd.Series([543,234], index=['Megha', 'Durga'])
print(data_)

'''2.Accessing by index
--------------------
--> By accessing with the index value and will get data of the that index
eg-- '''
import pandas as pd
data_=pd.Series([543,234], index=['Megha', 'Durga'])
print(data_['Megha'])

'''--> we convert a normal dictionary into a structure data by pandas
eg-- '''
import pandas as pd
stu={'name':'Megha',
     'age':21,
     'Batch':7
     }
det=pd.Series(stu)
print(det)

'''DataFrame
---------
--> A dataframe is known as two dimensional labeled data structure in pandas and which contains rows and columns
--> to convert data into structured data, the data should be given in the dict
--> in the values we pass list of data
eg-- '''

import pandas as pd
details={
    'Brand':['Apple','VIVO','realme'],
    'Product':['Mobile','Buds','Powerbank'],
    'Price':[45000, 2500, 1800]
    }
out_c=pd.DataFrame(details)
print(out_c)

import pandas as pd
details={
    'Brand':['Apple','VIVO','realme'],
    'Product':['Mobile','Buds','Powerbank'],
    'Price':[45000, 2500, 1800]
    }
out_c=pd.DataFrame(details)
print(out_c['Price'])


import pandas as pd
details={
    'Brand':['Apple','VIVO','realme'],
    'Product':['Mobile','Buds','Powerbank'],
    'Price':[45000, 2500, 1800]
    }
out_c=pd.DataFrame(details)
print(out_c[['Price','Brand']])

'''Methods
-------
head()
------
--> we get the first 5 rows
eg-- '''

import pandas as pd
details={
    'Brand':['Apple','VIVO','realme','Samsung', 'Nothing', 'redmi'],
    'Product':['Mobile','Buds','Powerbank', 'watch', 'Mobile', 'charger'],
    'Price':[45000, 2500, 1800, 1000, 17500, 8000]
    }
out_c=pd.DataFrame(details)
print(out_c.head())

'''tail()
------
--> we get last 5 rows
eg-- '''

import pandas as pd
details={
    'Brand':['Apple','VIVO','realme','Samsung', 'Nothing', 'redmi'],
    'Product':['Mobile','Buds','Powerbank', 'watch', 'Mobile', 'charger'],
    'Price':[45000, 2500, 1800, 1000, 17500, 8000]
    }
out_c=pd.DataFrame(details)
print(out_c.tail())

'''shape
-----
--> used to find the number of rows and columns
eg-- '''

import pandas as pd
details={
    'Brand':['Apple','VIVO','realme','Samsung', 'Nothing', 'redmi'],
    'Product':['Mobile','Buds','Powerbank', 'watch', 'Mobile', 'charger'],
    'Price':[45000, 2500, 1800, 1000, 17500, 8000]
    }
out_c=pd.DataFrame(details)
print(out_c.shape)

'''info()
------
--> this method will give us total information about data present
eg-- '''
import pandas as pd
details={
    'Brand':['Apple','VIVO','realme','Samsung', 'Nothing', 'redmi'],
    'Product':['Mobile','Buds','Powerbank', 'watch', 'Mobile', 'charger'],
    'Price':[45000, 2500, 1800, 1000, 17500, 8000]
    }
out_c=pd.DataFrame(details)
print(out_c.info())


'''Data Cleaning
-------------
--> Data cleaning is the process of finding problem and fixing it to analyse data properly
1.Missing values
2.Incorrect data

isnull()
--------
--> This method can find any null values present in the data, then it written True
eg-- '''
import pandas as pd
details={
    'Brand':['Apple','VIVO','realme','Samsung', 'Nothing', 'redmi'],
    'Product':['Mobile',None,'Powerbank', 'watch', 'Mobile', 'charger'],
    'Price':[45000, 2500, 1800, 1000, 17500, None]
    }
out_c=pd.DataFrame(details)
print(out_c.isnull())


'''dropna()
--------
--> used to remove the null valued rows from the data
eg-- '''
import pandas as pd
details={
    'Brand':['Apple','VIVO','realme','Samsung', 'Nothing', 'redmi'],
    'Product':['Mobile',None,'Powerbank', 'watch', 'Mobile', 'charger'],
    'Price':[45000, 2500, 1800, 1000, 17500, None]
    }
out_c=pd.DataFrame(details)
print(out_c.dropna())


'''sum()
-----
--> Method can find number of null values present in the data
syntax --> variable_name.isnull().sum()
eg-- '''

import pandas as pd
details={
    'Brand':['Apple','VIVO','realme','Samsung', 'Nothing', 'redmi'],
    'Product':['Mobile',None,'Powerbank', None, 'Mobile', 'charger'],
    'Price':[45000, 2500, 1800, 1000, 17500, None]
    }
out_c=pd.DataFrame(details)
print(out_c.isnull().sum())

'''duplicated()
------------
--> If any same data present it will identify and writen True
eg-- '''

import pandas as pd
details={
    'Brand':['Apple','Apple','realme','Samsung', 'Nothing', 'redmi'],
    'Product':['Mobile','Mobile','Powerbank', None, 'Mobile', 'charger'],
    'Price':[45000, 45000, 1800, 1000, 17500, None]
    }
out_c=pd.DataFrame(details)
print(out_c.duplicated())

'''read.csv()
----------
--> This can read the csv file data
syntax --> pd.read_csv(file_name)
eg-- 

import pandas as pd
readfile=pd.read_csv('students.csv')
print(readfile)



import pandas as pd
readfile=pd.read_csv('students.csv')
print(readfile.duplicated()) '''



























