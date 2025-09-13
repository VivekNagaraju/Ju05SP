'''
Created on 13-Sep-2025

Encapsulation:

Capsule?
'''

class Student:
    
    school_name = "iQuest" # Defining Class variable outside of methods/ constructor
    def __init__(self, name, roll_no): # Constructor with parameters
        print(f"A new Student {name} is enrolled for {Student.school_name} with roll_no {roll_no}")
        self._name = name # Protected Variable
        self.__roll_no = roll_no # Private variable
        # Student.school_name = "iQuest" # # Defining Class variable inside a method/ constructor
    
    def calculate_percentage(self, kan, eng, sci):
        per=((kan+eng+sci)/300)*100
        print(f"Pass percentage of {self.name} is: {per}%")

std1 = Student("Vivek", 101)
print(std1._name)
std1._name = "Vivek Culprit"
print(std1._name)

print(dir(std1))
print(std1._Student__roll_no)
std1._Student__roll_no = 420
print(std1._Student__roll_no)
