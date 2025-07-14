'''
Created on 13-Jul-2025

Looping statements: Looping statements are used to execute any statement/s repeatedly until
                    a condition fulfilled

Types of looping statements:
1. While loop: used to execute any statement/s repeatedly
    a. Initialize a variable
    b. Defining condition using 'while' keyword
    c. Increment/ decrement
    
2. For loop: used to iterate over a collection/ range

Loop control statements/ keywords:
1. Break: it breaks the execution of a loop upon some condition is met 
2. Continue: skips the current execution of a loop based on a condition
'''
'''
count=0

while count<5:
    print("My name is Vivek")
    # count=count+1 # increase count value by 1
    count+=1 # increase count value by 1
'''
'''
count=10
while count>0:
    print(count)
    count-=1
    if count == 5:
        break
'''

count=10
while count>0:
    
    if count == 5:
        count-=1
        continue
    
    print(count)
    count-=1
    

# print(range(10))
'''
for i in range(2, 100, 2):
    print(i)
    if i == 50:
        break
'''
'''
for i in range(2, 100, 2):
    if i == 50:
        continue
    print(i)
'''