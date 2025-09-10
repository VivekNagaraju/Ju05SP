'''
Created on 08-Sep-2025

Inheritance: Transferring/passing of properties/attributes from parent/super class to child/sub class

Types of Inheritance:
1. Single level inheritance: GrandParent -> Father
2. Multi-level inheritance: GrandParent -> Father -> Child
3. Multiple inheritance: Father & Mother -> Child

mro() - Method Resolution Order
'''
class GrandParent:
    def __init__(self, name):
        self.name = name
        print("This is GP constructor")
        print(f"{self.name} object is created")
        
    def gp_method(self):
        print("This is GP method")
        
class Father(GrandParent):
    def __init__(self,name, dob):
        print("This is Father class constrcutor")
        print(f"{name} is born on {dob}")
        super().__init__(name)
        
    def f_method(self):
        print("This is Father method")
        
    def car(self):
        print("This is Father's car")
        
class Mother:
    def m_method(self):
        print("This is Mother method")
        
    def car(self):
        print("This is Mother's car")

class Child(Father, Mother):
    def c_method(self):
        print("This is child method")

print("======GrandParent Class=======")
ajji = GrandParent("ajji")  
ajji.gp_method()    

print("======Father Class=======")
appa = Father("appa", "23/98/4653")
appa.f_method()
appa.gp_method()

print("======Child Class=======")
nanu = Child("paapu", "23/87/5678")
nanu.c_method()
nanu.f_method()
nanu.gp_method()
nanu.m_method()
nanu.car()

print("======mro for Child Class Object=======")
print(Child.mro())

print("=========dir()=========")
print(dir(nanu))