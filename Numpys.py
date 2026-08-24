""" Data Analysis

--> Data Analysis is the process of collecting,cleaning,transforming,organizing and analyzing data to convert
into useful information and also used for making decisions to get better outcome

--> Library Used:

Numpy
Pandas
matplotib
seabon

Numpy:

-->This refers to numerical python
-->It is an python library used for calculations and operations
-->This python library is more faster than the list to perform operations
--> And also this supports mult-dimension arrays

Ex:Single dimension

import numpy as np
arr=np.array([1,2,3,4,5])
print(arr.ndim) 
 

Functions:

1.ndim

-->The function is used to find out the dimensions of an array
-->Syntax: arr.ndim
ex:

import numpy as np
arr_2=np.array([[1,2,3,4,5]])
print(arr_2.ndim)
arr_3=np.array([[[1,2,3],[4,5,6],[7,8,9]]])
print(arr_3.ndim)

2.shape

--> The shape function is used to find out rows and col of an array
--> Syntax: arr.shape
ex:

import numpy as np
arr_2=np.array([1,2,3,4,5])
print(arr_2.shape)
arr_3=np.array([[1,2,3],[4,5,6]])
print(arr_3.shape)

3.reshape

--> The function is used to convert one dimension to another if the elements are there convert into the any dimension
-->Syntax: array.reshape(row,col)
ex:

import numpy as np
arr_2=np.array([1,2,3,4,5,6])
print(arr_2.reshape(2,3))
arr_3=np.array([1,2,3,4,5,6,7,8,9])
print(arr_3.reshape(3,3))

4.size

--> The size functions is used to find out the number of elements present in an array
-->Syntax: array.size

import numpy as np
arr_2=np.array([1,2,3,4,5,6])
print(arr_2.size)

5.arrange

--> The arrange function is used to generate numbers in a sequence upto certain limit and it form 1D array
--> And this array can convert into 2D array by using reshape
--> Syntax:np.arange(range)

import numpy as np
arr_2=np.arange(1,10)
print(arr_2)

import numpy as np
arr_=np.arange(1,10)
arr_2=arr_.reshape(3,3)
print(arr_2.ndim)
print(arr_)

Operations:

1.indexing:
--> Same as list we can also perform some operations on arrays like
1. indexing
2. slicing
3. add
4. sub

1. indexing

import numpy as np
arr_2=np.array([12,3,4,5,8,9,7])
print(arr_2[5])

2. slicing 

import numpy as np
arr_2=np.array([12,3,4,5,8,9,7])
print(arr_2[2:5])

3. add 

import numpy as np
arr_2=np.array([1,2,3,4,5,6])
arr=np.array([7,8,9,10,11,12])
print(arr_2+arr)
print(arr_2+5)

4. sub

import numpy as np
arr_2=np.array([1,2,3,4,5,6])
arr=np.array([7,8,9,10,11,12])
print(arr_2-arr)
print(arr-5)

5.mul

import numpy as np
arr_2=np.array([1,2,3,4,5,6])
print(arr_2*2)

6. power 

import numpy as np
arr_2=np.array([1,2,3,4,5,6])
print(arr_2**3)

7. Div 

import numpy as np
arr_2=np.array([1,2,3,4,5,6])
print(arr_2/2)

8.max 

import numpy as np
arr_2=np.array([1,2,3,4,5,6])
print(arr_2.max()) """

















