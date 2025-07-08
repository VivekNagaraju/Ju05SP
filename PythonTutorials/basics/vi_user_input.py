'''
Created on 08-Jul-2025

User input: Taking input from the user instead of hard coding

Hard coding- passing values in the program itself

+ b/w strings --> Concatenation (combining 2 strings)
+ b/w numerical data types --> mathematical addition

Input function takes any input value and stores/converts it as string.


'''
a=int(input("Please enter an integer:"))
b=int(input("Please enter another integer:"))
print("Type of a",type(a))
print("Type of b",type(b))
c=a+b
print(f"Sum of {a} and {b} is",c)

