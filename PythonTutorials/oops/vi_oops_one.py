'''
Created on 12-Aug-2025

Class creation:

Syntax: 

class ClassName:
    def method_one(self):
        pass
        
        
class --> Keyword
ClassName --> Each word of a ClassName should be capitalized(First letter should be in upper case, all other letters
are in lower case). If there are multiple words in a ClassName they are not separated with space/underscore.
method_one --> method is a function defined inside a class

'''

from oops.vi_types_of_variables import city
print(city)

class Student:
    def annouce_the_creation(self, name):
        print(f"A new Student object {name} is created")
        
student1 = Student() # creation of an Object called student1 from Student class
student1.annouce_the_creation("Vivek")

print(type(student1)) # <class '__main__.Student'>
# student1 --> Object
# Student --> Class

print(dir(student1))