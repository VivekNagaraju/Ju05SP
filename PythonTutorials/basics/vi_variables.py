'''
Created on 06-Jul-2025

Variables: Name given to memory location/ container where data is stored

Value/ data stored in the memory location keeps changing

We use these variable names as reference to access the data stored in the container

Syntax:

variable_name = value

Invalid cases:

48 = num7 --> variables names should always be on left hand side

1stnum = 87 --> Variable names shouldn't start with numbers

Comments: Statements used to provide explanation for a code. 

Comments are not considered by python interpreter during execution.

1. Multi-line commenting: 
we use triple single quotes(''' ''')/ double quotes(""" """) before and after the set of code
2. Single-line commenting: we add hashtag(#) before each line of code
'''



student = "Vivek"
print("Student name is",student)

num1 = 34
num2 = 67
print(num1, num2)
print(f"Sum of {num1} and {num2} is",num1+num2)

'''Defining multiple variables in single line'''

num3, num4 = 28, 15
print(num3+num4)
#print(num3) 


'''When multiple variables store same data/ value'''
num5 = num6 = 20
print(num5)
print(num6)


num_list = 10, 20, 30, 40
print(num_list)
print(type(num_list)) # <class 'tuple'>

print('{a}, {0}, {abc}'.format(10, a=2.5, abc=[1,2]))

a = 10
b = a

print(id(a))
print(id(b))

b = 20
print("a-->", a)
print(id(a))
print("b-->", b)
print(id(b))
