#import calculator file
from calculator import calculator
#make class
class renielcalculator(calculator):
#inherit
    def __init__(self):
        super().__init__()
#more operators
    def remainder_operation(self, integer1, integer2):
            remainder = integer1 % integer2
            return remainder

    def exponent_operation (self, integer1, integer2):
            exponent = integer1 ** integer2
            return exponent
