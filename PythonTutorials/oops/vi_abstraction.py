'''
Created on 13-Sep-2025

Abstraction: something existing in thought or as an idea but not having a physical or concrete existence

If a feature/ method differs in its implementation in different child/ sub classes we just define an
unimplemented method in parent/ super class and declare it as abstract method.

Thus, any class having one or more abstract method is called as abstract class.

From an abstract class, object can't be created (An abstract class can't be instantiated)

So it makes mandatory for Child classes to provide implementation for an abstract method.

Interface: If a class contains only abstract methods then it is called as an Interface

Note:
- All unimplemented methods are not abstract methods but all abstract methods are unimplemented
'''
from abc import ABC, abstractmethod

class Car(ABC):
    def move_forward(self):
        print("Car is moving forward")
       
    @abstractmethod    
    def drive_train(self):
        pass
    
class HatchBackCar(Car):
    def move_backward(self):
        print("Car is moving backward")
        
    
    def drive_train(self):
        print("Front wheel drive is implemented")
        

swift=HatchBackCar()
swift.move_forward()
swift.drive_train()

car1 = Car()