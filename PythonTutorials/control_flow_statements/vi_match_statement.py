'''
Created on 12-Jul-2025

@author: admin
'''

choice = int(input("""Do you want convert from:
                1. Celsius to Fahrenhit
                2. Fahernhit to Celsius"""))

match choice:
    case 1:
        print("Converted to Fahrenhit")
    case 2:
        print("Converted to Celsius")
    case _:
        print("Please enter 1 or 2")