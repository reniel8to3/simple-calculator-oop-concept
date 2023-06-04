#import user_interface and calculator
from user_interface import user_interface 
from calculator import calculator
from inheritance import renielcalculator

interface = user_interface()
calc = calculator()
rencalculator = renielcalculator()
#user input if they want to try again
user_interface.print_statement
try_again='y'
while try_again=='y':
    user_interface()
#ask operation
    try:    
        integer1 = interface.integer1()
        print ()
        integer2 = interface.integer2()
        print()
    except ValueError:
        print("There seems to be an error. Are you sure you entered an integer?")
        print ()
        continue
    main_operation = interface.what_operation()
    # addition
    try:
        if main_operation == "1":
            sum = calc.addition (integer1, integer2)
            interface.sum_operation(sum)
    #subtraction
        elif main_operation == "2":
            difference = calc.subtraction (integer1, integer2)
            interface.difference_operation(difference)

        # using the multiply function
        elif main_operation == "3":
            product = calc.multiplication (integer1, integer2)
            interface.product_operation(product)

        # using the division function
        elif main_operation == "4":
            quot = calc.division (integer1, integer2)
            interface.quot_operation (quot)

        # using the remainder function
        elif main_operation == "5":
            rem = rencalculator.remainder_operation (integer1, integer2)
            interface.rem_operation (rem)

        # using the remainder function
        elif main_operation == "6":
            exp = rencalculator.exponent_operation (integer1, integer2)
            interface.exp_operation (exp)

        else:
            print ("There seems to be an error. Are you sure you entered an integer?")
            continue
        #adding value error and zero division error
    except ZeroDivisionError:
        print("You can't divide by zero. Please try again")
        print ()
        continue
    # asking user if they want to try the program again
    try_again = input("Do you want to try again? Type y if yes and n if no.")
    if try_again =='n':
        print ('Thank you for using this program.')
        print ()
        break
