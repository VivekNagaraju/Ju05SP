'''
Created on 02-Aug-2025

Strings:

Single line string:
    Single double quotes
    Single single quotes

Multi-line strings:
    Triple double quotes
    Triple single quotes
    
My name is "Vivek"
'''
string1="MynameisVivek"

string2="""Multi-line strings:
    Triple double quotes
    Triple single quotes"""
    
print("string1: ", string1)
print("string2: ", string2)

string3='My name is "Vivek"'
print("string3: ", string3)

print("len(string3):", len(string3))
print("string3[3]: ",string3[3])

# string3[3] = "o" # TypeError: 'str' object does not support item assignment - immutable


string4= string3.capitalize()
print("string3 after capitalize:", string4)

string5 = string3.casefold()
print("string3 after casefold:", string5)

string6 = string3.center(38, "=")
print("string3 after centering", string6)

print(string3.endswith('"Vivek"'))

print(string3.find("v"))
print(string3.find("x"))

print(string3.index("v"))
# print(string3.index("x")) # ValueError: substring not found

print(string3.isalnum())
print(string1.isalpha())

string7 = " ".join(["Today", "is", "Saturday"])
print("string7:", string7)

print(string3.split(" "))
print("split(" ", 1)-->",string3.split(" ", 3))

print(string6.strip("="))
print(string6.lstrip("="))
print(string6.rstrip("="))

print(string3.partition(" "))
print("partition('*')-->",string3.partition("*"))

print(string3.rpartition(" "))
print(string2.splitlines())
print(string2.splitlines(keepends=True))

string8='My\n name is\n "Vivek"'
print("string8:", string8)

print(string3.title())