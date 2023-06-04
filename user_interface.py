#user interface
class user_interface():
    #print statement
    def print_statement(self):
        print ("This program is designed to function as a simple calculator. This program can perform Addition, Subtraction, Multiplication, and Division.")
    #ask user for input
    def integer1 (self):
        integer1 = int(input('Input the first integer: '))
        return integer1
    def integer2 (self):
        integer2 = int(input('Input the second integer: '))
        return integer2
    #ask for operation
    def what_operation (self):
        operation = input("What do you want the program to solve? 1 - Addition. 2 - Subtraction. 3 - Multiplication. 4- Division. 5 - Remainder. 6 - Exponent")
        return operation
    # show answer for addition
    def sum_operation (self, sum):
        print("The sum of your input is ", str(sum))

    # show output for subtraction
    def difference_operation (self, difference):
        print("The difference of your input is ", str(difference))

    # define multiplication functions
    def product_operation (self, product):
        print("The product of your input is ", str(product))

    # define division function
    def quot_operation (self, quot):
        print("The quotient of your input is ", str(quot))

    # define division function
    def rem_operation (self, rem):
        print("The remainder of your input is ", str(rem))

    # define division function
    def exp_operation (self, exp):
        print("The exponent of your input is ", str(exp))

