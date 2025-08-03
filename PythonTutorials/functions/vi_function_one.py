'''
Created on 03-Aug-2025

@author: admin
'''
def welcome(name):
    print(f"Hi {name}, Welcome to programming!!")
  
def find_length(ds):
    count=0
    for i in ds:
        count+=1
    
    # print(count)
    return count
  
welcome("Vivek")
find_length([1, 2, 3, 4, 5, 6])
print(find_length([1, 2, 3, 4, 5, 6]))



