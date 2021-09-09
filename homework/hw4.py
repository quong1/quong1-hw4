# ASSIGNMENT: The below is a common design pattern that can be cleaned up.
# We have a lengthy mathematical operation that uses a few pieces of
# information several times in order to mutate a value. This code organization
# isn't inherently wrong, but it does result in some pretty messy callsites,
# especially once we introduce nested function calls in compound_op_it().
# 
# The goal of this assignment is to refactor the below into a class: 
# 1) Shared arguments between functions should become instance variables of the class
# in order to minimize clutter (because now they won't have to be arguments
# to each function). 
# 2) The class should have a function self.complicated_math_operation()
# that accomplishes everything complicated_math_operation() currently does.
# 3) There's a design decision lurking in here! Should we make the starting_value
# an instance variable of the class that each function call mutates, or should we
# keep the current structure where complicated_math_operation() accepts a starting value
# and repeatedly mutates it? Leave a comment explaining which one you chose
# and under what circumstances that might make sense. There's no right answer! 

import math

class ComplicatedMathOperation:
    
    #default class constructor
    def __intit__(self, min_value, max_value, coefficient):
        self.min_value = min_value
        self.max_value = max_value
        self.coefficient = coefficient

    #multiply function
    def multiply_it(self, starting_value):
        return max(self.min_value, min(self.max_value, starting_value * self.coefficient))
    
    #addition function
    def add_it(self, starting_value):
        return max(self.min_value, min(self.max_value, starting_value + self.coefficient))
    
    #square root function
    def sqrt_it(self, starting_value):
        return max(self.min_value, min(self.max_value, math.pow(starting_value, -self.coefficient)))
    
    #compound operation function, doing addition function after multiply function
    def compound_op_it(self, starting_value):
        return self.add_it(self.multiply_it(starting_value))

    #complicated math operation function, perform all functions on starting value
    def complicated_math_operation(self,starting_value):
        res = starting_value
        res = self.multiply_it(res)
        res = self.add_it(res)
        res = self.sqrt_it(res)
        res = self.compound_op_it(res)
        return res

    # I keep the current structure where complicated math operation function repeatedly mutate the starting 
    # value instead of making starting_value an instance of a class that each function call mutates because
    # performing all the functions on starting_value is not always what the user want. Making starting_value
    # as an instance of the class ensure that the users want to perform all functions on the value entered,
    # while keeping the current structure enables the users to pick and choose what functions they want to
    # perform on the value entered.