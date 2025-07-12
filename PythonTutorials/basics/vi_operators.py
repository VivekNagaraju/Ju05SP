'''
Created on 08-Jul-2025

Operator: performs operation

Operation: task performed by operator

Operand: on which operation in performed by an operator

Operator: is a symbol which performs operation on one or more operands

Classification based on Operands:
1. Unary Operator: performs operation on a single operand
Ex: minus operator used for negating the input values
a=6
b=-4

2. Binary Operator: performs operation on 2 operands. Ex: +, -, * etc.,

3. Ternary Operator: performa operation on 3 operands. Ex: conditional statements

Types of OPerators:

1. Arithmetic Operators: +, -, multiplication(*), division(/), modulus (%), exponent (**), floor/ integer division(//)
    modulus operator gives reminder of division operation
    i/p -> numeric
    o/p -> numeric
    
2. Relational/ comparison operators: >, <, <=, >=, !=, ==
    i/p -> numeric
    o/p -> boolean
    
3. Assignment operator: =
4. Logical operators: and, or, not
    i/p -> boolean
    o/p -> boolean
    
5. Membership operators: operator checks whether any particular element is part of bigger collection
    in, not in
    Ex:
    'v' in 'vivek' --> True
    'a' not in 'vivek' --> True
    
    i/p -> element and collection
    o/p -> boolean
    
6. Identity Operators: operator checks whether two elements/ variables are one and the same
    is, is not
    Ex:
    'Vivek' is not 'vivek' --> True
    
    i/p -> anything
    o/p -> boolean
'''

print("=====Arithmetic OPerators=====")
num1 = 6
num2 = 3
num3 = 1.0
num4 = 4

print(f"Sum of {num1} and {num2} is", num1+num2)
print(f"Sum of {num3} and {num2} is", num3+num2)
print(f"Difference of {num1} and {num2} is", num1-num2)
print(f"Difference of {num1} and {num3} is", num1-num3)

print(f"Product of {num1} and {num2} is", num1*num2)
print(f"Product of {num1} and {num3} is", num1*num3)
print(f"Division of {num1} and {num2} is", num1/num2)
print(f"Division of {num1} and {num3} is", num1/num3)
print(f"Division of {num1} and {num4} is", num1/num4)

# Do addition, subtraction, multiplication and division b/w complex and other numerical data types

print(f"Modulus of {num1} and {num4} is", num1%num4)
print(f"{num2} power of {num4} is", num2**num4)
print(f"Floor/ Integer Division of {num1} and {num4} is", num1//num4)

print("=====Relational/ comparison operators====")
print(f"Is {num1} greater than {num2}?", num1>num2)
print(f"Is {num3} greater than {num2}?", num3>num2)

# Try different comparison operators

print("=====Logical operators=====")
bool1 = True
bool2 = False

print(f"{bool1} and {bool2} is", bool1 and bool2)
print(f"{bool1} and {bool1} is", bool1 and bool1)
print(f"{bool2} and {bool2} is", bool2 and bool2)
print(f"{bool2} and {bool1} is", bool2 and bool1)

# Try or operator

print(f" not {bool1} is", not bool1)
print(f" not {bool2} is", not bool2)

print("======Membership operators======")
print("Is 'v' in 'vivek'?", 'v' in 'vivek')
print("Is 'V' in 'vivek'?", 'V' in 'vivek')
print("Is 'v' not in 'vivek'?", 'v' not in 'vivek')
print("Is 'V' not in 'vivek'?", 'V' not in 'vivek')

print("=======Identity Operators=======")
num5 = 6
num6 = 6.0
print(id(num5))
print(id(num6))

print(f"{num5} and {num6} are identical -->", num5 is num6)
print(f"{num5} and {num6} are not identical -->", num5 is not num6)

print("================")
print(4+3%5)
print(2**(3**2))
print((2**3)**2)
print(2**3**2)