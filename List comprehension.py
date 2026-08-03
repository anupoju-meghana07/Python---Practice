""" List Comprehension :

The comprehension is the short form of syntax used to generate a new list from the old list

syntax: [expression loop] """

num=[1,2,3,4,5]
new_l=[j if j % 2 == 0 else 'odd' for j in num]
print(new_l) #['odd', 2, 'odd', 4, 'odd']

nel_=[i for i in num if i % 2 !=0]
print(nel_) #[1, 3, 5]

""" Nested Comprehension :

--> Nested Comprehension means an comprehension inside the another comprehension is called nested comprehension
--> Syntax: [expression loop_1 and loop_2] """

match = [[1,2,3],[4,5,6],[7,8,9]]
any_ = [i for i in match]
all_ = [num for j in match for num in j]
print(any_) #[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(all_) #[1, 2, 3, 4, 5, 6, 7, 8, 9]


new_= [[i*j for j in range(1,6)] for i in range(1,6)]
ne = [i for i in range(1,6)]
print(ne)   #[1, 2, 3, 4, 5]
print(new_) #[[1, 2, 3, 4, 5], [2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20], [5, 10, 15, 20, 25]]

"""--> Generator

-->This generator will generate values one at a time and pause it on the position when we are using yield keyword
-->Here we will use yield to get the value

--> yield Keyword :

-->This yield() is used to get the value and will only gives one value and pauses there itself

--> next Keyword :

--> the next() will retrieve the value """

def gen(n):
    for i in range(1,n+1):
        yield i*i
a = gen(5)
print(next(a)) #1
print(next(a)) #4
print(next(a)) #9

"""Function

--> return():
-- When the return is executed , it will exit for the function
--> In func will get all values once

Generator

--> yield():
-- When the yield is executed , it will pause the function and the next yield is called then it will resume again
--> In generator will get one at a time """




