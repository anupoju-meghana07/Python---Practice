""" Regular Expression (RegEx)

--> This RegEx is used to form a searching pattern to find out the string contain sequence char or not
--> To use this RegEx, we need to import re module

Functions :
1.Findall
2.Search

1.Findall:

-->This searching pattern is found then,it will gives the o/p in the list[]

import re
some='Python is programming language'
print(re.findall('[a]',some))

2.Search:

-->This is also used to form a search pattern, but it will give only the first matched object
-->Where it will gives with the index position,where the matched object is found by the pattern 

import re
do='I have 1000 rupees with me'
print(re.search('e',do))

-->Meta Characters:

--> Meta Characters are the symbols used in the search pattern
1. []
2. .
3. +
4. ^
5. $
6. ?
7. *
8. {}

1. []:

-->This [] is used to find the group of value,characters that are present in the string where we can also specify the range
--> Syntax : re.findall('[range]',variable_name)
--> By using this we can search A-Z,a-z and digits(0-9)

import re
some='We are in the class7'
print(re.findall('[aitc]',some))
print(re.findall('[a-z]',some))
print(re.findall('[A-Z]',some))
print(re.findall('[0-9]',some))
print(re.search('[a-z]',some))

2. .:

--> This symbol will refer only one means can match only a single char in the pattern
--> Syntax: re.search('C...',variable_name)

import re
some='Hello! World'
print(re.findall('H...o',some))
print(re.search('H....',some))
print(re.search('....o',some)) 

3. + :
--> The symbol max number of sequence from the dtring from atleast one character
--> Syntax : re.findall('.+',variable_name)


import re
some='The symbol is used to find a program '
print(re.findall('T.+r',some))
 

4. ^ :

--> The symbol is used to find pattern where string starting (word or letter) matching or not
--> Syntax: re.findall('^',variable_name)

import re
some='Hello! World'
print(re.search('^Hello',some))
print(re.search('^World',some))
print(re.findall('^Hello',some))

5. $ :

--> This symbol will find out if the string is ending with pattern or not
--> re.finall('sequenc$',variable_name)

import re
any_ = 'I am Planning a trip'
print(re.findall('trip$',any_))
print(re.search(' a trip$',any_))


6. ? :

--> The symbol will find max upto 1 match in the string
-->syntax: re.findall('.?',variable_name)

import re
some='Hello! World Hello'
print(re.findall('Hel.?o',some)) 

7. * :

-->The symbol max number of sequence from the string
-->Syntax re.findall('.*',variable_nname)

import re
some='The symbol is used to find a char that present'
print(re.findall('T.*r',some))

8. {} :

--> The symbol is used  to find a group char that present in string
--> Syntax: re.findall('E.{size}',variable_name)

import re
all_='I have 1000 ruppes with me'
print(re.findall('I.{2,}',all_))
print(re.findall('I.{2}',all_))

------Name Validation----

import re
user_name=input("Enter your name")
pattern=re.search('^[A-Z,a-z]{3,}$',user_name)
if pattern:
    print('Correct')
else:
    print('Incorrect')

----Phone Number(India or not)-----

import re
num=input("Please enter a number")
fnd=re.findall('^[6-9][0-9]{9}$',num)
if fnd:
    print('Indian')
else:
    print('Not Indian') """


















