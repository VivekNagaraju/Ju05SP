'''
Created on 08-Sep-2025

Types of variables:

1. Local variables(Method level variables): Scope is restricted to one particular method
2. Instance variables(Object level variables)
3. Static Variables(Class level variables)
4. Global variables
'''
city = "Mysuru"
class Student:
    
    school_name = "iQuest" # Defining Class variable outside of methods/ constructor
    def __init__(self, name, roll_no): # Constructor with parameters
        print(f"A new Student {name} is enrolled for {Student.school_name}, {city} with roll_no {roll_no}")
        self.name = name
        self.roll_no = roll_no
        # Student.school_name = "iQuest" # # Defining Class variable inside a method/ constructor
    
    def calculate_percentage(self, kan, eng, sci):
        per=((kan+eng+sci)/300)*100
        print(f"Pass percentage of {self.name} is: {per}%")
    
obj1 = Student("Vivek", 101)
obj1.calculate_percentage(100, 35, 75)
obj1.calculate_percentage(100, 50, 100)
print(obj1.name)
print(Student.school_name)

obj2 = Student("Sansri", 202)
obj2.calculate_percentage(100, 100, 100)
