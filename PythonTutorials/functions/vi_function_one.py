'''
Created on 03-Aug-2025

@author: admin

Fibonacci series: 0, 1, 1, 2, 3, 5, 8, 13....
'''
def welcome(name):
    print(f"Hi {name}, Welcome to programming!!")

def list_creation(value):
    i = 1
    list1 = []
    while i <= value:
        list1.append(i)
        i += 1
    return list1
  
def find_length(ds):
    # welcome("Vivek")
    count=0
    for i in ds:
        count+=1
    
    # print(count)
    return count
  
def find_length_create(value):
    ds = list_creation(value)
    count = find_length(ds)
    
    return ds, count
    
find_length([1, 2, 3, 4, 5, 6])
print(find_length([1, 2, 3, 4, 5, 6]))


#list_creation(user_input)
# print(list_creation(4))
print(find_length(list_creation(4)))

print(find_length_create(10))
x, y = find_length_create(20)
print(x)
print(y)
