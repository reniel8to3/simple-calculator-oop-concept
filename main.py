#import user_interface and calculator
from user_interface import userinterface 
from calculator import calculator

interface = userinterface()
calc = calculator()
#user input if they want to try again
try_again='y'
while try_again=='y':
    userinterface()
#ask operation
try:    
    integer1 = interface.integer1()
    print ()
    integer2 = interface.integer2()
    print()
#adding value error and zero division error
except ZeroDivisionError:
    print("You can't divide by zero. Please try again")
except ValueError:
    print("There seems to be an error. Are you sure you entered an integer?")