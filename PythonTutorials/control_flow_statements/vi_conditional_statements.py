'''
Created on 12-Jul-2025

Conditional statements: 
 Condition defined in this statement decides flow of execution
 
 Types:
 
 1. If statement
 2. If-else statement
 3. Series if-else statements (else-if statements)

Indentation: Space given at beginning of any statement to define a block/ group of code

1 indentation = 1 tab space/ 4 normal spaces
'''
age=int(input("Please enter your age:"))

'''
if age>18:
    print("Allow inside")
else:
    print("Don't allow")
'''    
'''
if age <= 0:
    print("Please give valid input")
elif age<13:
    print("You're child")
elif age<= 18:
    print("You're a teenager")
elif age <= 60:
    print("You're an adult")
else:
    print("You're a senior citizen")
'''

if age <= 0:
    print("Please enter valid input")
elif age > 18:
    if age > 60:
        print("You're a senior citizen")
    else:
        print("You're an adult")
else:
    if age<13:
        print("You're a child")
    else:
        print("You're a teenager")


    
    
    