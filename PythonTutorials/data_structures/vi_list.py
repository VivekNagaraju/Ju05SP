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
print(type(list1))

'''Creation of list with elements'''
list2 = [1, 2, 3, 4, 5] # homogeneous list
print("list2 -->", list2)
print(type(list2))

'''Creation of list using built-in function'''
list3 = list(range(10))
print("list3 -->", list3)
print(type(list3))
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
del(list3[5])
print(list3)

'''List specific predefined functions'''
list3.append(15)
print("After appending list3 with 15:",list3)

list3.append(list2)
print("After appending list3 with list2:",list3)

# list3.clear()
# print("list3 after clearing:", list3)

print("list3 copied into list6:", list6)

print("count of 4 in list3:",list3.count(4))

print("count of 2.3 in list5:",list5.count(2.3))

list3.extend(list2)
print("After extending list3 with list2:",list3)

print("count of 4 in list3:",list3.count(4))

print("list3[9]",list3[9])
print("list3[10]",list3[10])
print("list3[11]",list3[11])


    