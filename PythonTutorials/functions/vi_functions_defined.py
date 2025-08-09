'''
Created on 09-Aug-2025

@author: admin
'''
def welcome(name): # creation of function
    print(f"Hi {name}, Welcome to programming!!")
    
def list_creation(value):
    i = 1
    list1 = []
    while i <= value:
        list1.append(i)
        i += 1
    return list1

def find_length(ds):
    # welcome("Vivek") # calling a function inside another function
    count=0
    for i in ds:
        count+=1
    
    # print(count)
    return count # returning the o/p instead of printing to console