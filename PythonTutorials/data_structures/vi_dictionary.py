'''
Created on 26-Jul-2025

@author: Vivek

Dictionary: We store data in key-value pairs within '{}'

Syntax:
    {key1:value1, key2:value2, key3:value3.....}
    
1. Empty dictionary can be created
2. Dictionary can be created with built-in function 'dict()' using keyword arguments
3. Dictionary don't allow duplicate elements
4. When there is duplicate key with different values are present, 
    last value is assigned to that key.
5. When there are elements with different keys but same value are present,
    both the elements are retained/accepted as it is
6. Dictionary can be mutable(modifiable)
'''
dict1={}
print('dict1-->',dict1)
print('Type of dict1',type(dict1))

dict2={1:"Ganashree", 2:"Kannada Kasturi", 3:"Nithin"}
print('dict2-->',dict2)

dict3=dict(one="Ganashree", two="Kannada Kasturi")
print('dict3-->',dict3)

dict4={1:"Ganashree", 2:"Kannada Kasturi", 3:"Nithin", 3:"Nithin"}
print('dict4-->',dict4)

dict5={1:"Ganashree", 2:"Kannada Kasturi", 3:"Nithin", 3:"Vivek"}
print('dict5-->',dict5)

dict6={1:"Ganashree", 2:"Kannada Kasturi", 3:"Nithin", 4:"Nithin"}
print('dict6-->',dict6)

print("""==========Accessing the elements==========""")
"""Using Keys"""
# print(dict6[0]) #KeyError
print(dict6[1]) #Ganashree
# print(dict6["Ganashree"]) #KeyError

print("""=====Using for loop=====""") # access/ iterate over the keys of a dictionary
for i in dict6:
    print(i)

print("========Slicing Operator=======")
# print(dict6[1:3]) # TypeError: unhashable type: 'slice'

print("========Modification=========")
print('dict6 before modification-->',dict6)
dict6[4]="Vivek"
print('dict6 after modification-->',dict6)
dict6[50]="Shreyas" # if key doesn't exist new element will be added
print('dict6 after adding new element-->',dict6)

l=list('HELLO') # ['H', 'E', 'L', 'L', 'O']
l[0]='H'
l[-1]='O'
l[1:3]=['E','L']
p='H', 'O', ['E', 'L'] #('H', 'O', ['E', 'L']) --> packing of tuple
print('a={0}, b={1}, c={2}'.format(*p)) # *p--> unpacking the tuple

i=1
while True:
    if i%0O12 == 0: # 0O12 --> octal number == 10 in decimal number
                    # implicitly octal number is converted to decimal number
        break
    print(i)
    i += 1
'''    
d={0:'a', 1:'b', 2:'c'}
for x, y in d:
    print(x,y)
    
for i in range(2.0):
    print(i)
'''
'''Predefined functions'''
print("======fromkeys======")   
dict7=dict6.fromkeys([1.0, 2.0, 3.0, 4.0], "dummy") #Create a new dictionary with keys from iterable and values set to value.
print("dict6-->", dict6)
print("dict7-->", dict7)

print("======get()======")
print(dict6.get(4, "Key is not present")) # Return the value for key if key is in the dictionary, else default.
print(dict6.get(5, "Key is not present"))

print("=======items()======")
print(dict6.items())

print("=======keys()======")
print(dict6.keys())

print("=======values()======")
print(dict6.values())

print("=======iterating over values of a dictionary======")
for i in dict6.values():
    print(i)
    
print("=======update() from a dictionary======")
print("dict6-->", dict6)
print("dict7-->", dict7)    
dict6.update(dict7)
print("dict6 after update(dict7)", dict6)

print("=====Update from an iterable=====")
dict7.update([(1, 'Ganashree'), (2, 'Kannada Kasturi'), (3, 'Nithin'), (4, 'Vivek'), (50, 'Shreyas')])
print("dict7-->", dict7)  

print("======Update from keyword arguments======")
dict6.update(one="Sanjana", two="Sharina", ten="Tejas")
print("dict6-->", dict6)

