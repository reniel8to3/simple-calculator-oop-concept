#user interface
class userinterface:
    #print statement
    def print_statement(self):
        print ("This program is designed to function as a simple calculator. This program can perform Addition, Subtraction, Multiplication, and Division.")
    #ask user for input
    def integer1 (self):
        int(input('Input the first integer: '))
        return integer1
    def integer2 (self):
        int(input('Input the second integer: '))
        return integer2
    #ask for operation
    def what_operation (self):
        operation = input("What do you want the program to solve? 1 - Addition. 2 - Subtraction. 3 - Multiplication. 4- Division. ")
        return operation
    # show answer for addition
    def sum_operation (self, sum):
        print("The sum of " , integer1, "and ", integer2, "is ", addition(integer1, integer2))

    # show output for subtraction
    def difference_operation (self, difference):
        print("The difference of " , integer1, "and ", integer2, "is ", subtraction(integer1, integer2))

    # define multiplication functions
    def product_operation (self, product):
        print("The product of " , integer1, "and ", integer2, "is ", multiplication(integer1, integer2))

    # define division function
    def quotient_operation (self, quotient):
        print("The quotient of " , integer1, "and ", integer2, "is ", division(integer1, integer2))
