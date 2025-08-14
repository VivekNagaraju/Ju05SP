'''
Created on 14-Aug-2025

Constructor: 

__init__() --> It is a magic method used to construct an object

magic method --> It is a predefined method which has specific function to do

1. Constructor is called implicitly at the time of Object creation
2. Constructor can be called explicitly like any other method
3. Constructor can be with parameters or without parameters
4. It is not mandatory to define a constructor. When a class is defined without a constrcutor
    Python will have its own constructor defined.
    
Diff b/w Method and Constructor:
Method:
1. Method is used to define operations/actions/functions
2. Method can have any name
3. Method has to be called explicitly

Constructor:
1. Constructor is used to construct/ initialize an object with specific features
2. Constructor name should always be'__init__'
3. Constructor is called implicitly at the time of Object creation but it can be called 
explicitly too

'''
class Student:
    '''
    def __init__(self, name, roll_no): # Constructor with parameters
        print(f"A new Student object {name} is created with roll_no {roll_no}")
    '''
    
    def __init__(self): # Constructor without parameters
        print("A new student object is created")
        
student1 = Student()  
student1.__init__()     

        
        
       