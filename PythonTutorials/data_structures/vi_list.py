'''
Created on 22-Jul-2025

List:

Creation:
1. Empty 'List' can be created
2. List can be created with elements
    - Manually
      > homogeneous list - list containing same type of data elements
      > heterogeneous list - list contains diff. type of data elements
          List accepts None values
      > list can be created with duplicate elements
    - using built-in functions - list()/tuple()/set(), range()
    
Accessing elements from the list:
1. By using indexing --> ds_name[index]
2. By using slicing operator  --> ds_name[start index : stop index : step]
3. By using loops - for, while

List is mutable: existing list can be modified
'''

'''Creation of empty list'''
list1 = []
print("list1 -->", list1)
print(type(list1)) # <class 'list'>
# list1 --> Object
# list --> Class

'''Creation of list with elements'''
list2 = [1, 2, 3, 4, 5] # homogeneous list
print("list2 -->", list2)
print(type(list2))

'''Creation of list using built-in function'''
# list3 = list(range(10))
list3 = list({1, 2, 3, 4})
print("list3 -->", list3)
print("type(list3)", type(list3))
list6 = list3.copy()
'''Creation of heterogeneous list'''
list4 = [1, 2.4, 4+9j, "vivek", True, None] # heterogeneous list
print("list4 -->", list4)

'''Creation of list with duplicate elements'''
list5 = [1, 1,2.3, 2.3, "vivek", "vivek", True, True, None, None]
print("list5 -->", list5)

'''Accessing using Index'''
print("5th element in list5: ", list5[4])
print("5th element in list5: ", list5[-6])

'''Modification of existing list- Add/delete/replace(re-initialize)'''
list2[2] = 30
print("list2 -->", list2) # replace(re-initialize), existing list can be modified

'''
list2[5] = 6
print("list2 -->", list2) # IndexError: list assignment index out of range
'''
'''Accessing using for loop'''
for i in list4:
    print(i)
    
print('''=====Accessing using Slicing operator=====''')
print("list5 -->", list5)
print("list5[2:7] -->", list5[2:7])
print("list5[2:7:2] -->", list5[2:7:2])
print("list5[:7] -->", list5[:7])
print("list5[2:] -->", list5[2:])

print("=====Predefined functions======")
"""len()"""
print("len(list3):",len(list3))

"""del()"""
print(list3)
# del(list3[5])
print(list3)

'''List specific predefined functions'''
list3.append(15)
print("After appending list3 with 15:",list3)


print("list3+list2-->", list3+list2)
list3.append(list2)
print("After appending list3 with list2:",list3)

# list3.clear()
# print("list3 after clearing:", list3)

print("list3 copied into list6:", list6)

print("count of 4 in list3:",list3.count(4))

print("count of 2.3 in list5:",list5.count(2.3))

list3.extend(list2)
print("After extending list3 with list2:",list3)

print("Concatination of list3 and list2",list3+list2)

print("count of 4 in list3:",list3.count(4))

print("list3[9]",list3[9])
# print("list3[10]",list3[10])
# print("list3[11]",list3[11])

print("Index of 4 is",list3.index(4))
print("Index of 4 after 4 is",list3.index(4, 5))
# print("Index of 4 b/w 5 and 10 is",list3.index(4, 5, 10))  # ValueError: 4 is not in list
'''
Assignment:

1. Print a list to the user in the console (it should have duplicate elements)
2. Ask user to choose a element from the list
3. Print how many times that element is present in the list
4. Print the indices of that element in the list
5. Ask user to choose the index to remove the element present in that Index
    (Give one default option as All. If user chooses this you should remove the element from indices)
6. Ask user whether they want to repeat this exercise(Y/N)- 
    if yes repeat else terminate the program
    
    
Try to use arithmetic operators with list
'''
list3.insert(3, 45)
print("List3 after inserting 45 before index 3:", list3)

print("popping element at index 5:",list3.pop(5))
print("list3 after pop(5)", list3)

print("list3.pop(): ",list3.pop())
print("list3 after pop()", list3)

list3.remove(2)
print("list3 after removing 2:", list3)

list3.reverse()
print("list3 after reversing", list3)

list3.pop(4)
print("latest list3:", list3)

list3.sort()
print("list3 after sorting:", list3)

list3.sort(reverse=True)
print("sorting list in descending order:", list3)


'''Create a new list from list2 by multiplying 2 to each element'''
print("list2",list2)
list7=[]
for i in list2:
    list7.append(i*2)
print("list7:",list7)



'''List comprehension- precise way of creating a list'''
list8=[i*2 for i in list2]
print("list8:", list8)


print("======30/07/25=======")
a=[0,1,2,3]
for a[-1] in a: # 1. a[-1]=0 -> [0,1,2,0]; 2. a[-1]=1 -> [0,1,2,1]; 3. a[-1]=2 -> [0,1,2,2]; 4. a[-1]=2 -> [0,1,2,2]
    print(a[-1])
    print(a)

print(a*2)


names1 = ['Amir', 'Bear', 'Charlton', 'Daman']
names2 = names1 # call by reference --> whole object is passed --> original is modified
names3 = names1[:] # copy of names1 is created --> original will not be modified

print('names1: ', names1)
print(id(names1))
print('names2: ', names2)
print(id(names2))
print('names3: ', names3)
print(id(names3))


names2[0] = 'Alice' # ['Alice', 'Bear', 'Charlton', 'Daman']
names3[1] = 'Bob'    # ['Amir', 'Bob', 'Charlton', 'Daman']
# names1[0] = 'Alice2'

print('names1: ', names1)
print(id(names1))
print('names2: ', names2)
print(id(names2))
print('names3: ', names3)
print(id(names3))


names4=(1, 2, 3, 4)
names5=names4

print('names4: ', names4)
print(id(names4))
print('names5: ', names5)
print(id(names5))

