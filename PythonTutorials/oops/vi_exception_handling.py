'''
Created on 13-Sep-2025

@author: admin
'''
print(2+3)
print(4*3)

try:
   
    print(9/0)
    # raise NameError('HiThere')

except (TypeError, ZeroDivisionError) as tze:
    print(type(tze), ":", tze)
except Exception as e:
    print("Error occured in Line 11:", e, type(e))
"""   
except TypeError as te:
    print("TypeError:", te) 
    
except ZeroDivisionError as ze:
    print("ZeroDivisionError:", ze)
""" 


print(7-2)