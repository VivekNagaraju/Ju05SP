'''
Created on 09-Aug-2025

@author: admin

Import statements:

1. Importing individual function EX: from functions.vi_functions_defined import welcome
2. Importing multiple functions Ex: from functions.vi_functions_defined import welcome, list_creation
3. Importing all functions at a time Ex: from functions.vi_functions_defined import *
4. Aliasing: Ex: from functions.vi_functions_defined import list_creation as LC

'''
from functions.vi_functions_defined import list_creation as LC


# welcome("Vivek")
print(LC(9))
