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
1. By using indexing
2. By using slicing operator
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
    