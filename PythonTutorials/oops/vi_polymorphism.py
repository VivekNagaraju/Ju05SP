'''
Created on 10-Sep-2025

Polymorphism: Anything which appears in many forms

Poly = many
Morph = forms

'+' sign --> addition of numerics, list extension, string concatenation
'*' sign --> 

Types of Polymorphism:
1. Overloading:
    a. Operator overloading: An operator performs different operations based on the types of operands
    b. Method overloading: More than one method having same name but with different no./types of arguments
    c. Constructor overloading: A class having more than one constructor with different no./types of arguments
    
    - Both in Method overloading and Constructor overloading a particular method/ constructor is called
     based on no./types of arguments passed
    - But in Python strict Method overloading/ Constructor overloading is not supported
    - We need to find alternative ways for implementing Method overloading and Constructor overloading
        > Using default arguments
        > Using variable length arguments
        > Using variable length keyword arguments
        
2. Overriding:
    a. Method Overriding
    b. Constructor Overriding
'''

class Example:
    def add(self, a=0, b=0, c=0): # default arguments
        print(a+b+c)
    
    def add_infinite(self, *a): # Variable length arguments
        print(a)
ex1 = Example()
ex1.add_infinite()
ex1.add()
