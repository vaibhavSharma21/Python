''' SYNTAX AND SEMANTICS IN PYTHON'''
## Syntax refers to the set of rules that defines the combinations of symbols 
## that are considered to be correctly structured programs in a language.
## In simpler terms, syntax is about the correct arrangement of words and symbols 
## in a code.

## Semantics refers to the meaning or the interpretation of the symbols,characters,
## and commands in a language. It is about what the code is supposed to do when 
## it runs.

                    ## Basic Syntax Rules In Python
## Case sensitivity- Python is case sensitive

# name="Krish"
# Name="Naik"
# print(name)
# print(Name)

##---------------------------------------------------------------

''' INDENTATION '''
## Indentation in Python is used to define the structure and hierarchy of the code.
## Unlike many other programming languages that use braces {} to delimit blocks
## of code, Python uses indentation to determine the grouping of statements.
## This means that all the statements within a block must be indented at the
## same level.

## Indentation
## Python uses indentation to define blocks of code. Consistent use of spaces 
# (commonly 4) or a tab is required.

# age=32
# if age>30:
#     print(age)
# print(age)

##-----------------------------------------------------------------

''' Line Continuation '''
## Use a backslash (\) to continue a statement to the next line

# total=1+2+3+4+5+6+7+\
# 4+5+6
# print(total)

##-----------------------------------------------------------------

''' Multiple Statements on a single line '''

# x=5;y=10;z=x+y
# print(z)


''' Type Inference '''

# variable=10
# print(type(variable))
# variable="Krish"
# print(type(variable))

###-------------------------------------------------------------------------------

''' VARIABLES '''
## Variables are fundamental elements in programming used to store data 
## that can be referenced and manipulated in a program. In Python, variables 
## are created when you assign a value to them, and they do not need explicit
## declaration to reserve memory space. The declaration happens automatically
## when you assign a value to a variable.

## Naming Conventions
## Variable names should be descriptive
## They must start with a letter or an '_' and contains letter,numbers and underscores
## variables names case sensitive


# age='25'
# print(type(int(age)))


# name="Krish"
# print(int(name))   ### INVALID

##-----------------------------------------------------------------


#           ########## Dynamic Typing ########

## Python allows the type of a varible to change as the program executes

# var=10 
# print(var,type(var))

# var="Hello"
# print(var,type(var))

# var=3.14
# print(var,type(var))

##-----------------------------------------------------------------

''' input '''

# try:
#     age=int(input("What is the age"))
# except Exception as ex:
#     print(ex)
# else:
#     print(age,type(age))

##-----------------------------------------------------------------

''' Simple calculator '''

# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))

# sum = num1 + num2
# difference = num1 - num2
# product = num1 * num2
# quotient = num1 / num2

# print("Sum:", sum)
# print("Difference:", difference)
# print("Product:", product)
# print("Quotient:", quotient)


##-----------------------------------------------------------------

''' LOOPS '''
## for loop

# for i in range(5):
#     print(i)

##-----------------------------------------------------------------


# for i in range(1,10,2):
#     print(i)

##-----------------------------------------------------------------

# for i in range(10,0,-1):
#     print(i)

##-----------------------------------------------------------------


# for i in range(10,1,-2):
#     print(i)

##############---------------------------------------######################

## strings

# str="Vaibhav sharma"
# for i in str:
#     # print(i)
#     print(i,end='')  ## Vaibhav sharma

##-----------------------------------------------------------------

''' WHILE LOOP '''

## The while loop continues to execute as long as the condition is True.

# count=0
# while count<5:
#     print(count)
#     count=count+1

##-----------------------------------------------------------------

''' Loop Control Statements '''

## break
## The break statement exits the loop permaturely

# for i in range(10):
#     if i==5:
#         break
#     print(i)
   
##-----------------------------------------------------------------

''' continue '''

## The continue statement skips the current iteration and continues with the next.

# for i in range(10):
#     if i%2==0:
#         continue
#     print(i)

##-----------------------------------------------------------------

''' pass'''
## The pass statement is a null operation; it does nothing.

# for i in range(5):
#     if i==3:
#         pass
#     print(i)

##-----------------------------------------------------------------

'''Nested loops'''
## a loop inside a loop

# for i in range(3):
#     for j in range(2):
#         print(f"i:{i} and j:{j}")

##-----------------------------------------------------------------

## Examples- Calculate the sum of first N natural numbers using a while and for loop

## while loop  

# n=10   
# sum=0
# count=1
# while count<=n:
#     sum=sum+count
#     count=count+1
# print("Sum of first 10 natural number:",sum)

## SECOND APPROACH

# n=10   
# sum=0
# for i in range(11):
#     sum=sum+i

# print(sum)

##-----------------------------------------------------------------


## Example- Prime numbers between 1 and 100

# for num in range(1,101):
#     if num>1:
#         for i in range(2,num):
#             if num%i==0:
#                 break
#         else:
#             print(num)

##-----------------------------------------------------------------

''' INTRODUCTION TO LISTS '''

## * Lists are ordered, mutable collections of items.
## * They can contain items of different data types.

##### Video Outline:
# 1. Introduction to Lists
# 2. Creating Lists
# 3. Accessing List Elements
# 4. Modifying List Elements
# 5. List Methods
# 6. Slicing Lists
# 7. Iterating Over Lists
# 8. List Comprehensions
# 9. Nested Lists
# 10. Practical Examples and Common Errors

##-----------------------------------------------------------------

'''EMPTY LIST CREATE'''

# lst=[]
# print(type(lst))
# print(lst)

##-----------------------------------------------------------------

# names=["Krish","Jack","Jacob",1,2,3,4,5]
# print(names)

##-----------------------------------------------------------------

''' ACCESING THE ELEMENT'''

# fruits=["apple","banana","cherry","kiwi","gauva"]
# print(fruits[0])
# print(fruits[2])
# print(fruits[::]) ## they print the entire list
# print(fruits[-1])  
# print(fruits[1:])
# print(fruits[1:3])

##-----------------------------------------------------------------
 
'''' Modifying The List elements '''

# fruits=["apple","banana","cherry","kiwi","gauva"]
# fruits[1] = "watermelon"
# print(fruits)

##-----------------------------------------------------------------

''' List Methods '''

                ## APPEND METHOD ##

# fruits=["apple","banana","cherry","kiwi","gauva"]
# fruits.append("orange") ## Add an item to the end
# print(fruits)

##-----------------------------------------------------------------

                 ## INSERT METHOD ##

# fruits=["apple","banana","cherry","kiwi","gauva"]
# fruits.insert(1,"watermelon")
# print(fruits)

##-----------------------------------------------------------------

                 ## REMOVE METHOD ##

# fruits=["apple","banana","banana","cherry","kiwi","gauva"]
# fruits.remove("banana") ## Removing the first occurance of an item when list have duplicates items
# print(fruits)

##-----------------------------------------------------------------

                ## Remove and return the last element ##

# fruits=["apple","banana","banana","cherry","kiwi","gauva"]
# popped_fruits=fruits.pop()  ## pop works as LIFO
# print(popped_fruits)

##-----------------------------------------------------------------

                 ## INDEX METHOD ##

# fruits=["apple","banana","banana","cherry","kiwi","gauva"]
# index = fruits.index("cherry")
# print(index)

##-----------------------------------------------------------------
                 ## COUNT METHOD ##

# fruits=["apple","banana","banana","cherry","kiwi","gauva"]
# print(fruits.count('banana'))

##-----------------------------------------------------------------
                 ## SORT METHOD ##

# fruits=["banana","banana","cherry","kiwi","apple","gauva"]
# print(fruits.sort()) ## o/p = None
# x = fruits.sort()    
# print(fruits)      ### Note:  only this is valid 
# print(x)           ## o/p = None

##-----------------------------------------------------------------

                    ## REVERSE METHOD ##

# fruits=["banana","banana","cherry","kiwi","apple","gauva"]
# fruits.reverse()
# print(fruits)

##-----------------------------------------------------------------

                    ## CLEAR METHOD ##

# fruits=["banana","banana","cherry","kiwi","apple","gauva"]
# fruits.clear() ## Remove all items from the list
# print(fruits)

##-----------------------------------------------------------------

                  ## SLICING LIST ##

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(numbers[2:5])   ## 3,4,5
# print(numbers[:5])    ## 1,2,3,4,5
# print(numbers[5:])    ## 6,7,8,9,10
# print(numbers[::2]) ## 1,3,5,7,9
# print(numbers[::-1])  ## 10,9,8,8,7,6,5,4,3,2,1
# print(numbers[::-2])


##-----------------------------------------------------------------

                ### Iterating Over List ##

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for num in numbers:
#     print(num)

##-----------------------------------------------------------------

                ## Iterating with index

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for index,number in enumerate(numbers):
#     print(F"{index} : {number}")

##-----------------------------------------------------------------

'''LIST COMPRREHENSION '''

# Basics Syantax            [expression for item in iterable]

# with conditional logic    [expression for item in iterable if condition]

# Nested List Comprehension [expression for item1 in iterable1 for item2 in iterable2]



                    ## List comprehension  ####

# lst=[]
# for x in range(10):
#     lst.append(x**2)
# print(lst)

##------------

# x = [x**2 for x in range(10)]
# print(x)

# ##------------

# x = [(id,x**2) for id,x in enumerate(range(10))]
# print(x)

##-----------------------------------------------------------------

### LIST COMPREHENSION WITH IF CONDITION

# x = [i**2 for i in range(10) if i%2==0]
# print(x)

###--------------

# x = [(id,val**2) for id,val in enumerate(range(10)) if val%2==0]
# print(x)

##-----------------------------------------------------------------
                ## NESTED LIST COMPREHENSION ##

# lst1=[1,2,3]
# lst2=['a','b','c']
# pair=[[i,j] for i in lst1 for j in lst2]
# print(pair)

##-----------------------------------------------------------------

            ## List Comprehension with function calls

# words = ["hello", "world", "python", "list", "comprehension"]
# lengths = [len(word) for word in words]
# print(lengths)  # Output: [5, 5, 6, 4, 13]

##-----------------------------------------------------------------

#### Conclusion  ##
# List comprehensions are a powerful and concise way to create lists in Python. 
# They are syntactically compact and can replace more verbose looping constructs.
# Understanding the syntax of list comprehensions will help you write cleaner and more efficient Python code.
##-----------------------------------------------------------------
##-----------------------------------------------------------------

###############----------------------------------------------------------------##############

                              ###   TUPLES    ###

# Video Outline:
# 1. Introduction to Tuples
# 2. Creating Tuples
# 3. Accessing Tuple Elements
# 4. Tuple Operations
# 5. Immutable Nature of Tuples
# 6. Tuple Methods
# 7. Packing and Unpacking Tuples
# 8. Nested Tuples
# 9. Practical Examples and Common Errors

##-----------------------------------------------------------------

# ##### Introduction to Tuples

# Explanation:
# Tuples are ordered collections of items that are immutable.
# They are similar to lists, but their immutability makes them different.


## creating a tuple
# empty_tuple=()
# print(empty_tuple)
# print(type(empty_tuple))

##-----------------------------------------------------------------

                    #### TYPE CONVERION FROM LIST ---> TUPLE

# tp = list((1,2,3))
# print(type(tp))

##-----------------------------------------------------------------


# mixed_tuple=(1,"Hello World",3.14, True)
# print(mixed_tuple)

##-----------------------------------------------------------------

                    ## Accessing Tuple Elements 

# numbers = (1,4,5,6,8,12)
# print(numbers[2])
# print(numbers[-1])
# print(numbers[0:4])
# print(numbers[::-1])

##-----------------------------------------------------------------

                        ## Tuple Operations ##

# mixed_tuple=(1,"Hello World",3.14, True)
# numbers = (1,4,5,6,8,12)
# concatenation_tuple = numbers + mixed_tuple
# print(concatenation_tuple)

##-----------------------------------------------------------------


                         ## Tuple Methods  ##

# numbers = (1,4,1,5,6,8,12)
# print(numbers.count(1))
# print(numbers.index(5))

##-----------------------------------------------------------------

                        ## Packing and Unpacking tuple
# ## packing
# packed_tuple=1,"Hello",3.14
# print(packed_tuple)

# ##unpacking
# a,b,c = packed_tuple 
# print(a)
# print(b)
# print(c)

##-----------------------------------------------------------------------

                    ## Unpacking with *

# numbers=(1,2,3,4,5,6)
# first,*middle,last=numbers
# print(first)
# print(middle)
# print(last)

##-----------------------------------------------------------------------

                ## Nested List

# lst=[[1,2,3,4],[6,7,8,9],[1,"Hello",3.14,"c"]]
# lst[0][0:3]

##-----------------------------------------------------------------------
                ## Nested tuple

# nested_tuple = ((1, 2, 3), ("a", "b", "c"), (True, False))
# ## access the elements inside a tuple
# print(nested_tuple[0])
# print(nested_tuple[1][2])

##-----------------------------------------------------------------------
                    #### Conclusion ###

# Tuples are versatile and useful in many real-world scenarios where 
# an immutable and ordered collection of items is required. They are 
# commonly used in data structures, function arguments and return values, 
# and as dictionary keys. Understanding how to leverage tuples effectively 
# can improve the efficiency and readability of your Python code.
##-----------------------------------------------------------------------

''' SETS '''

# Sets are a built-in data type in Python used to store collections of 
# unique items. They are unordered, meaning that the elements do not 
# follow a specific order, and they do not allow duplicate elements. 
# Sets are useful for membership tests, eliminating duplicate entries,
#  and performing mathematical set operations like union, intersection,
# difference, and symmetric difference.

##-----------------------------------------------------------------------

                ## create a set ##

# my_set={1,2,3,4,5}
# print(my_set)
# print(type(my_set))

##-----------------------------------------------------------------------

                ## create a  empty set ##

# my_empty_set = set()
# print(type(my_empty_set))

##-----------------------------------------------------------------------

                ## TYPE CONVERSION OF LIST ---> SET ##

# my_set=set([1,2,3,4,5,6])
# print(my_set)

##-----------------------------------------------------------------------

                ## BASIC SET OPERATION
## Adiing Elements

# my_set=set([1,2,3,4,5,6])
# my_set.add(7)
# print(my_set)
# my_set.add(7)  ## DUPLICATES ARE NOT ALLOWED
# print(my_set)

##--------------


## Remove the elements from a set

# my_set=set([1,2,3,4,5,6])
# my_set.remove(3)
# print(my_set)

##--------------

## DIACARD OPERATION

# my_set=set([1,2,3,4,5,6])
# # my_set.remove(333) ## this gives error
# my_set.discard(333)  ## discard delete the element if it will present in the set
# print(my_set)

##-----------------------------------------------------------------------

                        ## pop method ##

# my_set=set([1,2,3,4,5,6])
# removed_element=my_set.pop()   ## it deleteds the random element
# print(removed_element)
# print(my_set)

##-----------------------------------------------------------------------

                        ## clear all the element ##

# my_set=set([1,2,3,4,5,6])
# my_set.clear()
# print(my_set)

##-----------------------------------------------------------------------

#                     ## Set Memebership test ##

# my_set={1,2,3,4,5}
# print(3 in my_set)
# print(10 in my_set)

##-----------------------------------------------------------------------

                      ## MAthematical Operation     
                       
# set1={1,2,3,4,5,6}
# set2={4,5,6,7,8,9}

# ### Union
# union_set=set1.union(set2)
# print(union_set)

# ## Intersection
# intersection_set=set1.intersection(set2)
# print(intersection_set)

# set1.intersection_update(set2)  ### It does not create a new set, it modifies set1 directly.
# print(set1)

##-----------------------------------------------------------------------

                        ## Difference  ##

# set1={1,2,3,4,5,6}
# set2={4,5,6,7,8,9}
# print(set1.difference(set2))
# print(set2.difference(set1))

# ## Symmetric Difference 
# ## This gives elements that are in either set1 or set2,
# ## but not in both (i.e., excluding common elements):
# x = set1.symmetric_difference(set2) 
# print(x)

##-----------------------------------------------------------------------

                    ## SET METHODS
# set1={1,2,3,4,5}
# set2={3,4,5}
# ## is subset
# print(set1.issubset(set2))
# print(set2.issubset(set1))
# print(set1.issuperset(set2))

##-----------------------------------------------------------------------

                   ### Counting Unique words in text ###

# text="In this tutorial we are are discussing about sets"
# words=text.split()
# ## convert list of words to set to get unique words
# unique_words=set(words)
# print(unique_words)
# print(len(unique_words))

##-----------------------------------------------------------------------
#                       #### Conclusion

# Sets are a powerful and flexible data type in Python that provide
# a way to store collections of unique elements. They support various
# operations such as union, intersection, difference, and symmetric
# difference, which are useful for mathematical computations. 
# Understanding how to use sets and their associated methods can 
# help you write more efficient and clean Python code, especially
# when dealing with unique collections and membership tests.
##-----------------------------------------------------------------------


''' DICTIONARIES '''

# Video Outline:
# 1. Introduction to Dictionaries
# 2. Creating Dictionaries
# 3. Accessing Dictionary Elements
# 4. Modifying Dictionary Elements
# 5. Dictionary Methods
# 6. Iterating Over Dictionaries
# 7. Nested Dictionaries
# 8. Dictionary Comprehensions
# 9. Practical Examples and Common Errors
##-----------------------------------------------------------------------

## Introduction to Dictionaries

# Dictionaries are unordered collections of items. They store data in key-value pairs.
# Keys must be unique and immutable (e.g., strings, numbers, or tuples), while values can be of any type.

##-----------------------------------------------------------------------

                    ## Creating Dictionaries
# APPROACH 1

# empty_dict = {}
# print(type(empty_dict))

# APPROACH 2
# empty_dict=dict()
# empty_dict


# student={"name":"Krish","age":32,"grade":24}
# print(student)
# print(type(student))

##-----------------------------------------------------------------------

                    # Single key is slways used

# student={"name":"Krish","age":32,"name":24}  ## THE KEY WHICH IS APPEND LATER IS REPLACE THE OLD KEY
# print(student)

##-----------------------------------------------------------------------

# student={"name":"VAIBHAV","age":22,"grade":'A'}
# print(student['grade'])
# print(student['age'])

# ## Accessing using get() method
# print(student.get('grade'))
# print(student.get('last_name'))  ## HERE IT GIVES THE O/P NONE
# print(student.get('last_name',"Not Available")) ## WE SET HERE NOT AVAILABLE BY DEFAULT

##-----------------------------------------------------------------------


                         ## Modifying Dicitonary Elements ##

## Dictionary are mutable,so you can add, update or delete elements

# student={"name":"VAIBHAV","age":22,"grade":'A'}
# print(student)
# student["age"]=33  ##update value for the key
# print(student)
# student["address"]="India" ## added a new key and value
# print(student)
# del student['grade'] ## delete key and value pair
# print(student)


##-----------------------------------------------------------------------

                                ## Dictionary methods ##

# student={"name":"VAIBHAV","age":22,"grade":'A'}
# keys=student.keys() ##get all the keys
# print(keys)
# values=student.values() ##get all values
# print(values)
# items=student.items() ##get all key value pairs
# print(items)

##-----------------------------------------------------------------------

                        ## shallow copy

# student={"name":"VAIBHAV","age":22,"grade":'A'}
# student_copy=student
# print(student)
# print(student_copy)

# student["name"]="Krish2"
# print("edit name",student)
# print("edit name",student_copy)

###--------

# student={"name":"VAIBHAV","age":22,"grade":'A'}
# print(" we perform shallow copy")
# student_copy1=student.copy() ## shallow copy
# print(student_copy1)
# print(student)

# student["name"]="KRish3"
# print(student_copy1)
# print(student)

##-----------------------------------------------------------------------

                            ### Iterating Over Dictionaries ###

## You can use loops to iterate over dictionatries, keys,values,or items

## Iterating over keys
# student={"name":"VAIBHAV","age":22,"grade":'A'}
# for keys in student.keys():
#     print(keys)

# ## Iterate over values
# for value in student.values():
#     print(value)

# ## Iterate over key value pairs
# for key,value in student.items():
#     print(f"{key}:{value}")

##-----------------------------------------------------------------------


                             ## Nested Disctionaries ##

# students={
#     "student1":{"name":"Krish","age":32},
#     "student2":{"name":"Peter","age":35}
# }
# print(students)
# ## Access nested dictionaries elementss
# print(students["student2"]["name"])
# print(students["student2"]["age"])
# print(students.items())

##-----------------------------------------------------------------------


                        ## Iterating over nested dictionaries ##

# students={
#     "student1":{"name":"Krish","age":32},
#     "student2":{"name":"Peter","age":35}
# }
# for student_id,student_info in students.items():
#     print(f"{student_id}:{student_info}")
#     for key,value in student_info.items():
#         print(f"{key}:{value}")

##-----------------------------------------------------------------------

                            ## Dictionary Comphrehension ##

# squares={x:x**2 for x in range(10)}
# print(squares)

##-----------------------------------------------------------------------

                        ## Condition dictionary comprehension ##

# evens={x:x**2 for x in range(10) if x%2==0}
# print(evens)

##-----------------------------------------------------------------------


                        ## Practical Examples

            ## USe a dictionary to count he frequency of elements in list

# numbers=[1,2,2,3,3,3,4,4,4,4]
# frequency={}

# for number in numbers:
#     if number in frequency:
#         frequency[number]+=1
#     else:
#         frequency[number]=1
# print(frequency)

##-----------------------------------------------------------------------

## Merge 2 dictionaries into one

# dict1={"a":1,"b":2}
# dict2={"b":3,"c":4}
# merged_dict={**dict1,**dict2}   ### duplicates keys are not allowed
# print(merged_dict)

##-----------------------------------------------------------------------
                            #### Conclusion
# Dictionaries are powerful tools in Python for managing key-value pairs.
#  They are used in a variety of real-world scenarios, such as counting 
# word frequency, grouping data, storing configuration settings, managing
# phonebooks, tracking inventory, and caching results. Understanding how 
# to leverage dictionaries effectively can greatly enhance the efficiency
# and readability of your code.
##-----------------------------------------------------------------------


''' Lambda Functions in Python '''

# Lambda functions are small anonymous functions defined using the 
# lambda keyword. They can have any number of arguments but 
# only one expression. They are commonly used for short operations
# or as arguments to higher-order functions.

            ###    Syntax  ####

# lambda arguments: expression

##-----------------------------------------------------------------------

                ### ADDITION USING LAMBDA FUNCTION ###
# def add(a,b):
#     return a+b
# x = add(2,3)
# print(f"sum is {x}")

# add = lambda a,b : a+b
# print(f"sum by using lambda function is {add(2,3)}")

##-----------------------------------------------------------------------

# def even(num):
#     if num%2==0:
#         return True 
# print(even(24))

# even1=lambda num:num%2==0
# print("using lambda function ",even1(12))

##-----------------------------------------------------------------------
##-----------------------------------------------------------------------

''' The map() Function in Python '''

# The map() function applies a given function to all items in an 
# input list (or any other iterable) and returns a map object 
# (an iterator). This is particularly useful for transforming
# data in a list comprehensively.

##-----------------------------------------------------------------------

                            ### SQUARE ROOT USING MAP FUNCTION ###
# def square(x):
#     return x*x
# print(square(10))

##------------------

# numbers = [1,2,3,4,5,6,7,8]
# sq = list(map(lambda x:x**2,numbers))  
# ## if we dont convert it into list then map function gives me the object
# print(sq)

##-----------------------------------------------------------------------

                        ### MAP MULTIPLE ITERABLES ###

# numbers1=[1,2,3]
# numbers2=[4,5,6]

# added_numbers=list(map(lambda x,y:x+y,numbers1,numbers2))
# print(added_numbers)

##-----------------------------------------------------------------------

#                 ### map() to convert a list of strings to integers ###
#                 ### Use map to convert strings to integers  ###
                
# str_numbers = ['1', '2', '3', '4', '5']
# int_numbers = list(map(int, str_numbers))

# print(int_numbers)  # Output: [1, 2, 3, 4, 5]

##-----------------------------------------------------------------------

#                   ## map() to convert a list of strings into uppercasse ###

# words=['apple','banana','cherry']
# upper_word=list(map(str.upper,words))
# print(upper_word)

##-----------------------------------------------------------------------

# people=[
#     {'name':'Krish','age':32},
#     {'name':'Jack','age':33}
# ]

# print(list(map(lambda people:people["name"],people)))

##-----------------------------------------------------------------------

#                        #### Conclusion
# The map() function is a powerful tool for applying transformations
# to iterable data structures. It can be used with regular functions,
#  lambda functions, and even multiple iterables, providing a versatile
#  approach to data processing in Python. By understanding and
#  utilizing map(), you can write more efficient and readable code.

##-----------------------------------------------------------------------
##-----------------------------------------------------------------------


''' The filter() Function in Python '''

# The filter() function constructs an iterator from elements of an iterable 
# for which a function returns true. It is used to filter out items from a 
# list (or any other iterable) based on a condition.

##-----------------------------------------------------------------------

# def even(num):
#     if num%2==0:
#         return True

# lst=[1,2,3,4,5,6,7,8,9,10,11,12]
# print(list(filter(even,lst)))

##-----------------------------------------------------------------------

                        ### filter with a Lambda Function ###

# numbers=[1,2,3,4,5,6,7,8,9]
# greater_than_five=list(filter(lambda x:x>5,numbers))
# print(greater_than_five)

##-----------------------------------------------------------------------

                    ### Filter with a lambda function and multiple conditions

# numbers=[1,2,3,4,5,6,7,8,9]
# even_and_greater_than_five = list(filter(lambda x:x>5 and x%2==0,numbers))
# print(even_and_greater_than_five)

##-----------------------------------------------------------------------

                   #### Filter() to check if the age is greate than 25 in dictionaries
# people=[
#     {'name':'Krish','age':32},
#     {'name':'Jack','age':33},
#     {'name':'John','age':25}
# ]
# ### filter() goes through each element in the iterable (people, which is a list of dictionaries).
# ##  For each element, it automatically calls your function (age_greater_than_25) with that element 
# ### as an argument.
# def age_greater_than_25(person):    
#     return person['age']>25

# print(list(filter(age_greater_than_25,people)))

##-----------------------------------------------------------------------

                            ##### Conclusion
# The filter() function is a powerful tool for creating iterators that filter
#  items out of an iterable based on a function. It is commonly used for data
# cleaning, filtering objects, and removing unwanted elements from lists.
# By mastering filter(), you can write more concise and efficient code for 
# processing and manipulating collections in Python.

##-----------------------------------------------------------------------
##-----------------------------------------------------------------------


''' Importing Modules in Python: Modules and Packages '''

# In Python, modules and packages help organize and reuse code. 
# Here's a comprehensive guide on how to import them.

##-----------------------------------------------------------------------

# import math
# print(math.sqrt(16))

##-----------------------------------------------------------------------

# from math import sqrt,pi
# print(sqrt(16))
# print(pi)

##-----------------------------------------------------------------------

# import numpy as np  ### pip install numpy
# x = np.array([1,2,3,4])
# print(type(x))
# print(x)

##-----------------------------------------------------------------------

# from math import *
# print(sqrt(16))
# print(pi)

##-----------------------------------------------------------------------

                    # #### Conclusion
# Importing modules and packages in Python allows you to organize
# your code, reuse functionalities, and keep your projects clean 
# and manageable. By understanding how to import modules, specific
# functions, and use relative imports within packages, you can 
# structure your Python applications more effectively.

##-----------------------------------------------------------------------
##-----------------------------------------------------------------------

''' Standard Library Overview '''

# Python's Standard Library is a vast collection of modules and 
# packages that come bundled with Python, providing a wide range 
# of functionalities out of the box. Here's an overview of some
# of the most commonly used modules and packages in the Python
# Standard Library.

##-----------------------------------------------------------------------

# import array
# arr=array.array('i',[1,2,3,4])  ## they take onlt two arguments
# print(arr)

##-----------------------------------------------------------------------

                ## RANDOM

# import random
# print(random.randint(1,10))
# print(random.choice(['apple','banana','cherry']))

##-----------------------------------------------------------------------

#                    ### File And Directory Access

# import os
# print(os.getcwd())
# os.mkdir('test_dir')  ## they make the directory in the folder whose name is test_dir

##-----------------------------------------------------------------------

                        ## Data Serialization
# Data serializability means converting a Python object (like a dictionary, list, etc.)
# into a format that can be stored or transferred — like a file, a string, or over the
# internet.
# import json
# data={'name':'Krish','age':25}

##-----------------------------------------------------------------------

                            ## JSON
# json_str=json.dumps(data)
# print(json_str)
# print(type(json_str))

# parsed_data=json.loads(json_str)
# print(parsed_data)
# print(type(parsed_data))

##-----------------------------------------------------------------------

#                             ## CSV

# import csv

# with open('example.csv',mode='w',newline='') as file:
#     writer=csv.writer(file)
#     writer.writerow(['name','age'])
#     writer.writerow(['Krish',32])

# with open('example.csv',mode='r') as file:
#     reader=csv.reader(file)
#     for row in reader:
#         print("the data is",row)

##-----------------------------------------------------------------------

#                             ## DATETIME

# from datetime import datetime,timedelta
# now=datetime.now()
# print(now)
# yesterday=now-timedelta(days=1)
# print(yesterday)

##-----------------------------------------------------------------------

#                             ## TIME

# import time
# print(time.time())
# time.sleep(10) ## here system sleep for 10 secconds
# print(time.time())

##-----------------------------------------------------------------------

#                        #### Conclusion

# Python Standard Library is extensive and provides tools for 
# almost any task you can think of, from file handling to
# web services, from data serialization to concurrent execution.
# Familiarizing yourself with the modules and packages available
#  in the Standard Library can significantly enhance your ability
#  to write efficient and effective Python programs.

##-----------------------------------------------------------------------
##-----------------------------------------------------------------------

''' File Operation- Read And Write Files '''

# File handling is a crucial part of any programming language.
# Python provides built-in functions and methods to read from 
# and write to files, both text and binary. This lesson will
# cover the basics of file handling, including reading and
# writing text files and binary files.

##-----------------------------------------------------------------------

#                            ### Read a Whole File

# with open('example.txt','r') as file:
#     content=file.read()
#     print(content)

##-----------------------------------------------------------------------

#                     ## Read a file line by line

# with open('example.txt','r') as file:
#     for l1 in file:
#         # print(l1)
#         print(l1.strip()) ## strip() removes the newline character

##-----------------------------------------------------------------------

#                   ## Writing a file(Overwriting)

# with open('example.txt','w') as file:
#     file.write('Hello World!\n')
#     file.write('this is a new line.')
# with open('example.txt','r') as file:
#     content = file.read()
#     print(content)

##-----------------------------------------------------------------------

                    ## Write a file(without Overwriting)

# with open('example.txt','a') as file:
#     file.write("\nAppend operation taking place!")

##-----------------------------------------------------------------------

#                    ### Writing a list of lines to a file

# lines=['First line \n','Second line \n','Third line\n']
# with open('example.txt','a') as file:
#     file.writelines(lines)

##-----------------------------------------------------------------------

#                         ### Binary Files

#                     # Writing to a binary file

# data = b'\x00\x01\x02\x03\x04'
# with open('example.bin', 'wb') as file:
#     print(file.write(data))

##-----------------------------------------------------------------------

#                      # Reading a binary file

# with open('example.bin', 'rb') as file:
#     content = file.read()
#     print(content)

##-----------------------------------------------------------------------

#       ### Read the content froma  source text fiile and write to a destination text file
#                           # Copying a text file

# with open('example.txt', 'r') as source_file:
#     content = source_file.read()

# with open('destination.txt', 'w') as destination_file:
#     destination_file.write(content)

##-----------------------------------------------------------------------

'''define of w+'''
# The w+ mode in Python is used to open a file for both 
# reading and writing. If the file does not exist, it
# will be created. If the file exists, its content is
# truncated (i.e., the file is overwritten).


#                 ### Writing and then reading a file

# with open('example.txt','w+') as file:
#     file.write("Hello world\n")
#     file.write("This is a new line \n")

#     ## Move the file cursor to the beginning
#     file.seek(0)

#     ## Read the content of the file
#     content=file.read()
#     print("now the read method executes\n")
#     print(content)

##-----------------------------------------------------------------------
##-----------------------------------------------------------------------

''' Working With File Paths '''

#  When working with files in Python, handling file paths correctly is
#  crucial to ensure your code works across different operating systems
#  and environments. Python provides several modules and functions for 
#  working with file paths effectively.

##-----------------------------------------------------------------------

#                   #### Using the os module

# import os
# cwd = os.getcwd()
# print(f"Current working directory is {cwd}")

##-----------------------------------------------------------------------

                        ## CREATE NEW DIRECTORY
# import os
# new_directory = "package"
# os.mkdir(new_directory)
# print(f"directory '{new_directory}' is created")

##-----------------------------------------------------------------------

#                             ## Listing Files And Directories

# import os
# print(os.listdir('.'))

##-----------------------------------------------------------------------

#                              ### Joining Paths
# import os
# dir_name="folder"
# file_name="file.txt"
# full_path = os.path.join(dir_name,file_name)
# print(full_path)

##-----------------------------------------------------------------------

# import os
# dir_name="folder"
# file_name="file.txt"
# full_path = os.path.join(os.getcwd(),dir_name,file_name)
# print(full_path)

##-----------------------------------------------------------------------

#                 ###  check whether the path of the file is exist or not

# import os
# paths = 'example.txt'
# if os.path.exists(paths):  ## here path is function and paths is variable
#     print(f"The path '{paths}' exists")
# else:
#     print(f"The path '{paths}' does not exists")

##-----------------------------------------------------------------------

#                     ## Checking if a Path is a File or Directory

# import os
# # path = 'example.txt'
# # path = "test_dir"
# path = input("Enter the path ")
# if os.path.isfile(path):
#     print(f"The path '{path}' is a file.")
# elif os.path.isdir(path):
#     print(f"The path '{path}' is a directory.")
# else:
#     print(f"The path '{path}' is neither a file nor a directory.")


##-----------------------------------------------------------------------

#                         ## Getting the absolute path

# import os
# relative_path='example.txt'
# absolute_path=os.path.abspath(relative_path)
# print(absolute_path)

##-----------------------------------------------------------------------
##-----------------------------------------------------------------------

''' Understanding Exceptions '''

# Exception handling in Python allows you to handle errors gracefully and
# take corrective actions without stopping the execution of the program.
# This lesson will cover the basics of exceptions, including how to use 
# try, except, else, and finally blocks.

##-----------------------------------------------------------------------

''' WHAT ARE EXCEPTIONS '''

#ANSWER:  Exceptions are events that disrupt the normal flow of a program.
#         They occur when an error is encountered during program execution. 

#  Common exceptions include:
    # - ZeroDivisionError: Dividing by zero.
    # - FileNotFoundError: File not found.
    # - ValueError: Invalid value.
    # - TypeError: Invalid type.

##-----------------------------------------------------------------------

                        ## Exception try ,except block

# a=b  ## give error

##-----------------------------------------------------------------------

# try:
#     a=b
# except NameError as ex:
#     print(ex)

##-----------------------------------------------------------------------

# try:
#     result = 5/0
# except ZeroDivisionError as ex:
#     print(ex)
#     print("Please enter the denominator greater than 0")

##-----------------------------------------------------------------------

# try:
#     result=1/2
#     a=b
# except ZeroDivisionError as ex:
#     print(ex)
#     print("Please enter the denominator greater than 0")
# except Exception as ex1:
#     print(ex1)
#     print('Main exception got caught here')

##-----------------------------------------------------------------------

# try:
#     num=int(input("Enter a number "))
#     result=10/num
# except ValueError:
#     print("This is not a valid number")
# except ZeroDivisionError:
#     print("enter denominator greater than 0")
# except Exception as ex:
#     print(ex)

##-----------------------------------------------------------------------

#                       ## try,except,else block

# try:
#     num=int(input("Enter a number:"))
#     result=100/num
# except ValueError:
#     print("That's not a valid number!")
# except ZeroDivisionError:
#     print("You can't divide by zero!")
# except Exception as ex:
#     print(ex)
# else:
#     print(f"the result is {result}")

##-----------------------------------------------------------------------

#                         ## try,except,else and finally
                        
# try:
#     num = int(input("Enter a number: "))
#     result = 10 / num
# except ValueError:
#     print("That's not a valid number!")
# except ZeroDivisionError:
#     print("You can't divide by zero!")
# except Exception as ex:
#     print(ex)
# else:
#     print(f"The result is {result}")
# finally:
#     print("Execution complete.")

##-----------------------------------------------------------------------
##-----------------------------------------------------------------------
##-----------------------------------------------------------------------
##-----------------------------------------------------------------------
##-----------------------------------------------------------------------
##-----------------------------------------------------------------------


''' NUMPY '''

# Numpy is a fundamental library for scientific computing in Python. 
# It provides support for arrays and matrices, along with a collection 
# of mathematical functions to operate on these data structures. 
# In this lesson, we will cover the basics of NumPy, focusing on 
# arrays and vectorized operations.

##-----------------------------------------------------------------------

#                 ## create array using numpy
#                     ##create a 1D array
# import numpy as np
# arr1 = np.array([1,2,3,4])
# print(arr1)
# print(type(arr1))
# print(arr1.shape)

##-----------------------------------------------------------------------

#                       ## 1 d array ----> 2d array

# import numpy as np
# arr2=np.array([1,2,3,4,5,6])  ## this in one dimension 
# print(arr2.reshape(1,6))  ## 1 row and 5 columns
# print(arr2.reshape(2,3))  ## 2 row and 3 columns

##-----------------------------------------------------------------------

#                   ## 2d array ----> 1d array

# import numpy as np
# arr2 = np.array([[1,2,3,4,5]])
# print(arr2.shape)

##-----------------------------------------------------------------------

#                     ## 2d array

# import numpy as np
# arr2=np.array([[1,2,3,4,5],[5,6,7,8,9]]) ### ye dono rows ke elements (a,b) (b,a) rule follow karne chahiye
# print(arr2)
# print(arr2.shape)

##-----------------------------------------------------------------------

                    ### arange function

# import numpy as np
# print(np.arange(0,10).reshape(5,2))

##-----------------------------------------------------------------------

# import numpy as np
# print(np.ones((3,3)))

##-----------------------------------------------------------------------

#                       ### IDENTIFY MATRIX

# import numpy as np
# print(np.eye(3))

##-----------------------------------------------------------------------

#                        ## Attributes of Numpy Array

# import numpy as np
# arr = np.array([[1, 2, 3], [4, 5, 6]])
# print("Array:\n", arr)
# print("Shape:", arr.shape)  # Output: (2, 3)
# print("Number of dimensions:", arr.ndim)  # Output: 2
# print("Size (number of elements):", arr.size)  # Output: 6
# print("Data type:", arr.dtype)  # Output: int64 (may vary based on platform)
# print("Item size (in bytes):", arr.itemsize)  # Output: 8 (may vary based on platform)

##-----------------------------------------------------------------------

#                           ### Numpy Vectorized Operation

# import numpy as np
# arr1=np.array([1,2,3,4,5])
# arr2=np.array([10,20,30,40,50])

# ### Element Wise addition
# print("Addition:", arr1+arr2)

# ## Element Wise Substraction
# print("Substraction:", arr1-arr2)

# # Element-wise multiplication
# print("Multiplication:", arr1 * arr2)

# # Element-wise division
# print("Division:", arr1 / arr2)


##-----------------------------------------------------------------------

#                        ## Universal Function

# import numpy as np
# arr=np.array([4,16,64,81,625])

# ## square root
# print(np.sqrt(arr))

# ## Exponential
# print(np.exp(arr))

# ## Sine
# print(np.sin(arr))

# ## natural log
# print(np.log(arr))

##-----------------------------------------------------------------------

#                        ## array slicing and Indexing

# import numpy as np
# arr=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
# print("Array : \n", arr)

##-----------------------------------------------------------------------

# import numpy as np
# arr=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
# print(arr[0:,0:])
# print(arr[0:,0:3])
# print(arr[1:,2:4])
# print(arr[0:2,2:3])

##-----------------------------------------------------------------------

#                              ## Modify array elements

# import numpy as np
# arr=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
# arr[0,0]=100
# print(arr)
# arr[1:] = 100
# print(arr)

##-----------------------------------------------------------------------

#                           ### statistical concepts--Normalization
#                       ## to have a mean of 0 and standard deviation of 1

# import numpy as np
# data = np.array([1, 2, 3, 4, 5])
# # Calculate the mean and standard deviation
# mean = np.mean(data)
# std_dev = np.std(data)
# # Normalize the data
# normalized_data = (data - mean) / std_dev
# print("Normalized data:", normalized_data)

##-----------------------------------------------------------------------

# import numpy as np
# data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# # Mean
# mean = np.mean(data)
# print("Mean:", mean)

# # Median
# median = np.median(data)
# print("Median:", median)

# # Standard deviation
# std_dev = np.std(data)
# print("Standard Deviation:", std_dev)

# # Variance
# variance = np.var(data)
# print("Variance:", variance)

##-----------------------------------------------------------------------

#                       ## Logical operation

# import numpy as np
# data=np.array([1,2,3,4,5,6,7,8,9,10])
# print(data[(data>=5) & (data<=8)])

##-----------------------------------------------------------------------
##-----------------------------------------------------------------------

''' Pandas-DataFrame And Series '''

# Pandas is a powerful data manipulation library in Python, widely used
# for data analysis and data cleaning. It provides two primary data
#  structures: Series and DataFrame. A Series is a one-dimensional 
# array-like object, while a DataFrame is a two-dimensional, size-mutable,
# and potentially heterogeneous tabular data structure with labeled axes 
# (rows and columns).

##-----------------------------------------------------------------------

#                                 ## Series ##
# ## A Pandas Series is a one-dimensional array-like object that can
# ## hold any data type. It is similar to a column in a table.

# import pandas as pd
# data=[1,2,3,4,5]
# series=pd.Series(data)
# print("Series \n",series)
# print(type(series))

##-----------------------------------------------------------------------

#                   ## Create a Series from dictionary

# import pandas as pd
# data={'a':1,'b':2,'c':3}
# series_dict=pd.Series(data)
# print(series_dict)

##-----------------------------------------------------------------------

# import pandas as pd
# data = [10,20,30]
# ind = ['a','b','c']
# print(pd.Series(data,index=ind))

##-----------------------------------------------------------------------

#                   ## Dataframe
# ## create a Dataframe from a dictionary oof list

# import pandas as pd
# data={
#     'Name':['Krish','John','Jack'],
#     'Age':[25,30,45],
#     'City':['Bangalore','New York','Florida']
#      }
# df = pd.DataFrame(data)
# print(df)
# print(type(df))

##-----------------------------------------------------------------------

# #                   ## Create a Data frame From a List of Dictionaries

# import pandas as pd
# data=[
#     {'Name':'Krish','Age':32,'City':'Bangalore'},
#     {'Name':'John','Age':34,'City':'Bangalore'},
#     {'Name':'Bappy','Age':32,'City':'Bangalore'},
#     {'Name':'JAck','Age':32,'City':'Bangalore'} 
#     ]
# df=pd.DataFrame(data)
# print(df)
# print(type(df))

##-----------------------------------------------------------------------

                ## HEAD AND TAIL ##

# import pandas as pd
# data=[
#     {'Name':'Krish','Age':32,'City':'Bangalore'},
#     {'Name':'John','Age':34,'City':'Bangalore'},
#     {'Name':'Bappy','Age':32,'City':'Bangalore'},
#     {'Name':'JAck','Age':32,'City':'Bangalore'} 
#     ]
# df=pd.DataFrame(data)
# print(df.head(2))
# print(df.tail(3))

##-----------------------------------------------------------------------

# import pandas as pd
# data={
#     'Name':['Krish','John','Jack'],
#     'Age':[25,30,45],
#     'City':['Bangalore','New York','Florida']
#      }
# df = pd.DataFrame(data)
# # print(df["Name"])
# # print(df.loc[0])
# # print(df.loc[1:3])

# # print(df.iloc[1,2])
# # print(df.iloc[0:2])

##-----------------------------------------------------------------------

#                         ## Accessing a specified element
# import pandas as pd
# data={
#     'Name':['Krish','John','Jack'],
#     'Age':[25,30,45],
#     'City':['Bangalore','New York','Florida']
#      }
# df = pd.DataFrame(data)
# print(df.at[2,'Age'])
# print(df.at[1,"Name"])

##-----------------------------------------------------------------------

#                 ## Accessing a specified element using iat
# import pandas as pd
# data={
#     'Name':['Krish','John','Jack'],
#     'Age':[25,30,45],
#     'City':['Bangalore','New York','Florida']
#      }
# df = pd.DataFrame(data)
# print(df.iat[2,2])

##----------------------------------------------------------------------

                    ## Adding a column

# import pandas as pd
# data={
#     'Name':['Krish','John','Jack'],
#     'Age':[25,30,45],
#     'City':['Bangalore','New York','Florida']
#      }
# df = pd.DataFrame(data)
# df["salary"] = [2300,5000,700000]
# print(df)

##-----------------------------------------------------------------------

# import pandas as pd
# data={
#     'Name':['Krish','John','Jack'],
#     'Age':[25,30,45],
#     'City':['Bangalore','New York','Florida']
#      }
# df = pd.DataFrame(data)
# #df.drop(0,inplace=True)
# df.drop("City",axis=1,inplace=True) ## if we dont write axis 1 then by default it
# print(df)                        ## checks the rows first and then gives the error
## here inplace permanentely delete the city column

##-----------------------------------------------------------------------

#                       ## modify age to the column

# import pandas as pd
# data={
#     'Name':['Krish','John','Jack'],
#     'Age':[25,30,45],
#     'City':['Bangalore','New York','Florida']
#      }
# df = pd.DataFrame(data)
# df['Age']=df['Age']+1
# print(df)

##-----------------------------------------------------------------------


# import pandas as pd
# df = pd.read_csv('data.csv')
# print(df.head(5))
# # Display the data types of each column
# print("Data types:\n", df.dtypes)
# ## describe function
# print(df.describe())
##-----------------------------------------------------------------------
##-----------------------------------------------------------------------

''' Data Manipulation and Analysis with Pandas '''

# Data manipulation and analysis are key tasks in any data science
# or data analysis project. Pandas provides a wide range of functions
# for data manipulation and analysis, making it easier to clean,
# transform, and extract insights from data. In this lesson,
# we will cover various data manipulation and analysis techniques 
# using Pandas.

##-----------------------------------------------------------------------

# import pandas as pd
# df = pd.read_csv(r"d:\python\data.csv")
# # print(pd.read_csv("data.csv").head(5))
# # print(df.head(5))
# # print(df.tail(5))
# # print(df.describe())
# # print(df.dtypes)

##-----------------------------------------------------------------------

#                         ## Handling Missing Values

# import pandas as pd
# df = pd.read_csv("data.csv")
# # print(df.isnull())    ###  isnull() tells that which values are null in the df
# # print(df.isnull().any()) ### isnull().any() gives False when the column has atleast one emty cell
# # print(df.isnull().sum())   ### isnull().sum() tells that how many cells are empty in each column
# # df_filled=df.fillna(0)   ### fillna() fill the empty cell like here empty cells are filled with 0
# # print(df_filled)

##-----------------------------------------------------------------------

#                       ### filling missing values with the mean of the column

# import pandas as pd
# df = pd.read_csv("data.csv")
# # print(df["Sales"].mean())  ### mean = 557
# df["sales_fillna"] = df["Sales"].fillna(df["Sales"].mean())
# print(df)

##-----------------------------------------------------------------------

#               ## Renaming Columns
# import pandas as pd
# df = pd.read_csv("data.csv")
# df=df.rename(columns={'Date':'Sales Date'})
# print(df.head)

##-----------------------------------------------------------------------

# ##              change datatypes

# import pandas as pd
# df = pd.read_csv("data.csv")
# df["Value_new"] = df["Value"].fillna(df["Value"].mean()).astype(int)
# # print(df.dtypes)
# print(df)

##-----------------------------------------------------------------------

# ###           apply function

# import pandas as pd
# df = pd.read_csv("data.csv")
# df['New Value']=df['Value'].apply(lambda x:x*2)
# print(df.head())


##-----------------------------------------------------------------------

#                       ## Data Aggregating And Grouping

# import pandas as pd
# df = pd.read_csv("data.csv")

# # # grouped_mean=df.groupby('Product')['Value'].mean()
# # # print(grouped_mean)

# # # grouped_sum=df.groupby(['Product','Region'])['Value'].sum()
# # # print(grouped_sum)

# ## aggregate multiple functions
# # groudped_agg=df.groupby('Region')['Value'].agg(['mean','sum','count'])
# # print(groudped_agg)

##-----------------------------------------------------------------------

###              Merging and joining Dataframes

# import pandas as pd
# df = pd.read_csv("data.csv")
# df1 = pd.DataFrame({'Key': ['A', 'B', 'C'], 'Value1': [1, 2, 3]})
# df2 = pd.DataFrame({'Key': ['A', 'B', 'D'], 'Value2': [4, 5, 6]})
# # print(df1)
# # print(df2)

# #           ## Merge Datafranme on the 'Key Columns'

# # print(pd.merge(df1,df2,on="Key",how="inner"))

# # print(pd.merge(df1,df2,on="Key",how="outer"))

# # print(pd.merge(df1,df2,on="Key",how="left"))

# # print(pd.merge(df1,df2,on="Key",how="right"))

##-----------------------------------------------------------------------
##-----------------------------------------------------------------------
##-----------------------------------------------------------------------


# import pandas as pd
# from io import StringIO
# Data = '{"employee_name": "James", "email": "james@gmail.com",\
#         "job_profile": [{"title1":"Team Lead", "title2":"Sr. Developer"}]}'
# df=pd.read_json(StringIO(Data))
# # print(df)
# # print(df.to_json())
# # print(df.to_json(orient='index'))   ### here we set the only index
# # print(df.to_json(orient='records'))


##-----------------------------------------------------------------------



# import pandas as pd
# df=pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data",header=None)
# print(df.head(5))
# #### Reason for header=None:
# #### You're telling Pandas not to treat the first row of the file as column headers,
# #### and instead treat all rows as data.

##-----------------------------------------------------------------------


# import pandas as pd
# url="https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/"
# df=pd.read_html(url)
# print(df[0])

##-----------------------------------------------------------------------


# import pandas as pd
# url="https://en.wikipedia.org/wiki/Mobile_country_code"
# df = pd.read_html(url,match="Country",header=0)
# print(df[0])

##-----------------------------------------------------------------------

###########   YE NAHI CHALEGA #########
# import pandas as pd
# df_excel=pd.read_excel('data.xlsx')
# df_excel.to_pickle('df_pickle')
# print(pd.read_pickle('df_excel'))

##-----------------------------------------------------------------------
'''MATPLOTLIB'''

# import matplotlib.pyplot as plt
# x=[1,2,3,4,5]
# y=[1,4,9,16,25]

# ##create a line plot
# plt.plot(x,y)  ### we can write print also
# plt.xlabel('X axis')
# plt.ylabel('Y Axis')
# plt.title("Basic Line Plot")
# plt.show()


##-----------------------------------------------------------------------

# ##                          create a customized line plot

# import matplotlib.pyplot as plt
# x=[1,2,3,4,5]
# y=[1,4,9,16,25]
# plt.plot(x,y,color='green',linestyle='-',marker='o',linewidth=2,markersize=6)
# plt.grid(True)
# plt.show()

##-----------------------------------------------------------------------


#                               ## Multiple Plots
#                                ## Sample data

# import matplotlib.pyplot as plt

# x = [1, 2, 3, 4, 5]
# y1 = [1, 4, 9, 16, 25]
# y2 = [1, 2, 3, 4, 5]

# plt.figure(figsize=(14,8))  #### figsize=(width,height)

# plt.subplot(2,2,1)        ### row=2 , column=2 , 1 means first top left subplot
# plt.plot(x,y1,color='green')
# plt.title("Plot 1")

# plt.subplot(2,2,2)
# plt.plot(y1,x,color='red')
# plt.title("Plot 2")

# plt.subplot(2,2,3)
# plt.plot(x,y2,color='blue')
# plt.title("Plot 3")

# plt.subplot(2,2,4)
# plt.plot(y2,y1,color='green')
# plt.title("Plot 4")

# plt.show()

##-----------------------------------------------------------------------

'''BAR PLOT'''

# import matplotlib.pyplot as plt
# categories = ['A','B','C','D']
# values = [4,8,2,6]
# plt.figure(figsize=(5,4))
# plt.bar(categories,values,color='crimson')  ## X,Y
# plt.show()


##-----------------------------------------------------------------------

''' Histograms '''

# Histograms are used to represent the distribution of a dataset.
# They divide the data into bins and count the number of data points 
# in each bin.

##-----------------------------------------------------------------------

####   Bin Width = (max-min )/ bin  =  (5-1)/5 = 0.8

                                    # Sample data

# import matplotlib.pyplot as plt
# data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]
# ##create a histogram
# plt.hist(data,bins=5,color='orange',edgecolor='black')
# plt.show()

##-----------------------------------------------------------------------



''' scatter plot '''
#                                # Sample data

# import matplotlib.pyplot as plt
# x = [1, 2, 3, 4, 5]
# y = [2, 3, 4, 5, 6]

# plt.scatter(x,y,color="blue",marker='x')
# plt.xlabel('x-axis')
# plt.ylabel('y-axis')
# # plt.grid(True) 
# plt.show()

##-----------------------------------------------------------------------

''' pie chart '''

# import matplotlib.pyplot as plt
# label=['A','B','C','D']
# sizes=[30,20,40,10]
# color=['gold','yellowgreen','lightcoral','lightskyblue']
# explode=(0.2,0,0,0) ##move out the 1st slice

# plt.pie(sizes,explode=explode,colors=color,labels=label,autopct='%1.1f%%',shadow=True)
# plt.show()

##-----------------------------------------------------------------------

#                          AUTOPCT
# '%': The string starts with a format instruction.
# '1.1f': This is Python's string formatting for floating-point numbers.
# 1 → Minimum width of the number (not so important here).
# .1 → One digit after the decimal point.
# f → Format as a floating-point number.
# '%%' → Escapes the % symbol to actually print %.

##-----------------------------------------------------------------------


'''data visualize sample'''

# import pandas as pd
# import matplotlib.pyplot as plt
# df= pd.read_csv("data.csv")
# # print(df.head())
# sales_data = df.groupby('Product')['Sales'].sum()
# print(sales_data)
# # plt.plot(sales_data,color='green')
# plt.plot(sales_data,color='green')

# plt.show()

##-----------------------------------------------------------------------
##-----------------------------------------------------------------------
''' SEABORN '''

# import seaborn as sb
# tips = sb.load_dataset('tips')
# print(tips)

##-----------------------------------------------------------------------


##                      create a scatter plot

# import seaborn as sb
# import matplotlib.pyplot as plt
# tips = sb.load_dataset('tips')
# sb.scatterplot(x='total_bill',y ='tip',data = tips)
# plt.show()


##-----------------------------------------------------------------------


''' line plot '''

# import seaborn as sb
# import matplotlib.pyplot as plt
# tips = sb.load_dataset('tips')
# sb.lineplot(x='size',y='total_bill',data=tips)
# plt.title("Line Plot of Total bill by size")
# plt.show()


##-----------------------------------------------------------------------

''' Bar Plot '''

# import seaborn as sb
# import matplotlib.pyplot as plt
# tips = sb.load_dataset('tips')
# sb.barplot(x='day',y='total_bill',data=tips)
# plt.title('Bar Plot of Total Bill By Day')
# plt.show()


##-----------------------------------------------------------------------

''' Box Plot '''

# import seaborn as sb
# import matplotlib.pyplot as plt
# tips = sb.load_dataset('tips')
# sb.boxplot(x="day",y='total_bill',data=tips)
# plt.show()

##-----------------------------------------------------------------------

''' Violin Plot '''

# import seaborn as sb
# import matplotlib.pyplot as plt
# tips = sb.load_dataset('tips')
# sb.violinplot(x='day',y='total_bill',data=tips)
# plt.show()

##-----------------------------------------------------------------------

''' Histograms '''

# import seaborn as sb
# import matplotlib.pyplot as plt
# tips = sb.load_dataset('tips')
# sb.histplot(tips['total_bill'],bins=10,kde=True)
# plt.show()

##-----------------------------------------------------------------------


''' KDE Plot '''

# import seaborn as sb
# import matplotlib.pyplot as plt
# tips = sb.load_dataset('tips')
# sb.kdeplot(tips['total_bill'],fill=True)
# plt.show()


##-----------------------------------------------------------------------

''' pairplot '''

# import seaborn as sb
# import matplotlib.pyplot as plt
# tips = sb.load_dataset('tips')
# sb.pairplot(tips)
# plt.show()

##-----------------------------------------------------------------------

''' Heatmap '''

# import seaborn as sb
# import matplotlib.pyplot as plt
# tips = sb.load_dataset('tips')
# corr=tips[['total_bill','tip','size']].corr()  ### firstly we corelate the columns
# sb.heatmap(corr,annot=True,cmap='coolwarm')  
# plt.show()


##-----------------------------------------------------------------------



##                           Plot total sales by product

# import pandas as pd
# import seaborn as sb
# import matplotlib.pyplot as plt
# import numpy as np
# df = pd.read_csv('data.csv')
# print(df.groupby('Product')['Sales'].mean())
# # sb.barplot(x='Product',y='Sales',data=df,estimator=sum)
# # sb.barplot(x='Product',y='Sales',data=df,estimator=len)
# # sb.barplot(x='Product',y='Sales',data=df,estimator=np.mean)
# # sb.barplot(x='Product',y='Sales',data=df,estimator=np.median)
# # sb.barplot(x='Product',y='Sales',data=df,estimator=np.var)
# # sb.barplot(x='Product',y='Sales',data=df,estimator=np.std)
# # sb.barplot(x='Product',y='Sales',data=df,estimator=np.min)
# # sb.barplot(x='Product',y='Sales',data=df,estimator=np.max)

# # plt.show()

##-----------------------------------------------------------------------
##-----------------------------------------------------------------------
##-----------------------------------------------------------------------

