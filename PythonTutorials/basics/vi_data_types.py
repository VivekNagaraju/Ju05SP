'''
Created on 07-Jul-2025

Data types: Types of data processed(input data) by a program or 
            generated(output data) by a program
            
Different categories of Data types in Python:
1. Built-in data types: Already present in python
    Fundamental data types
    - Integer
    - Float
    - Complex
    - String
    - Boolean
    
    Derived data types (Data structures)
    - List
    - Set
    - Tuple
    - Dictionary
    
    Miscellaneous
    - Bytes
    - Bytearray
    - None
    
2. User-defined data types: Created by users

type() --> built-in function used to determine the type of data stored in a variable

Dynamically typed: In python the type of data stored in a variable is determined during runtime

Type casting: Conversion of one type of data into another data type

Type casting is done using built-in functions listed below:
1. str(): converts to string
2. int(): converts to integer
3. float(): converts to float
4. complex(): converts to complex
5. bool(): converts to boolean
'''


student = "Vivek" # String
roll_no = 51 # Integer
age = 16.6 # Float
a = 4+5j # Complex
b = True # Boolean
c = False # Boolean
d = None # None type

print("Type of student is",type(student))
print("Type of roll_no is",type(roll_no))
print("Type of age is",type(age))
print("Type of a is",type(a))
print("Type of b is",type(b))
print("Type of c is",type(c))
print("Type of d is",type(d))

print("===============================")
'''Converting Integer to float'''
print("roll_no after converting to float",float(roll_no)) # o/p: 51.0

'''Converting Integer to complex'''
print("roll_no after converting to complex",complex(roll_no)) # o/p: (51+0j)

print("===============================")
'''Conversion of float to integer'''
print("age after converting to integer",int(age)) #o/p: 16

print("===============================")
'''Conversion of complex to integer'''
# print("a after converting to integer",int(a))

# o/p: TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'

