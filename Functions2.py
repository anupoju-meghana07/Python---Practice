""" Anonymous Function

--> Anonymous Func is a func that don't any have any name
--> This also called as lambda func
--> lambda func will take n number arguments but only one expression

Syntax: lambda arguments : expression """

so=lambda a:a+10
print(so(2))

so=lambda a,b,c:a+b+c
print(so(2,4,5))

"""--> map(): The map func will be applied on the given func of each and every element of an itterable"""

nums=[1,2,3,4,5]
so=list(map(lambda x:x*x,nums))
print(so)

"""-->filter(): filter() function will only consider if the cond is true ,then it will keep that values"""

nums=[1,2,3,4,5]
so=list(filter(lambda x:x%2==0,nums))
print(so)

"""-->reduce(): The reduce() func consider all elements and reduce to one single element

  --> to use reduce() we have to import it first from the functools """

from functools import reduce
nums=[1,2,3,4,5]
so=reduce(lambda x,y:x+y,nums)
print(so)

"""--> print():
print() is an in-built func that is used for display the values stored by values

--> return :
 --> only used inside the functions
 --> when the return is executed then it will exit from the function and holds the returned values in the calling """



