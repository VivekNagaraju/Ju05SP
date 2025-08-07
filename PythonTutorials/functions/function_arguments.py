'''
Created on 06-Aug-2025

Function argument: An argument is a variable/ parameter that is sent to the function as input.

Terms:

1. Formal arguments:
    - parameters defined inside parenthesis while defining the function
    - these arguments accepts/ receive the user input when calling the function
    
2. Actual arguments:
    - values/ variables passed while calling a function
    - these arguments are input data for a function
    
Ex: 

def welcome(name): # creation of function
    print(f"Hi {name}, Welcome to programming!!")
    
welcome("Vivek")

name --> Formal argument
"Vivek" --> Actual argument

Types of arguments:
Actual arguments:
    1. Positional arguments
    2. Keyword arguments
Formal arguments:
    1. Default arguments
    2. Variable length arguments
    3. Variable length keyword arguments
'''

def add(a=0, b=0, c=0): # default arguments
    print(a+b+c)
    
def sub(a, b):
    print(f"Difference b/w {a} and {b} is:", a-b)
    
def add_infinite(*a): # variable length arguments (positional arguments only, not keyword arguments)
    print(a)

def accept_infinite_kwrds(**a): # variable length keyword arguments
    print(a)
add()    
add(4)    
add(4, 5)
add(4, 5, 6)
# add(4, 5, b=10) # TypeError: add() got multiple values for argument 'b'

sub(6, 3) # a=6 ; b=3 # Positional arguments
sub(3, 6) # a=3 ; b=6

sub(b=3, a=6) # keyword arguments

add_infinite(1, 2, 3, 4, 5, 6)
add_infinite()

accept_infinite_kwrds(a=1, b=2, c=3)
