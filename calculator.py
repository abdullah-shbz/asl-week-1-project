import math 

class AdvanceCalculator:
    def __init__(self):
        self.history = [] # To store all our calculations
    def addition(self,a,b):
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    def subtraction(self,a,b):
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result
    def multiply(self,a,b):
        result = a * b
        self.history.append(f"{a} x {b} = {result}")
        return result
    def division(self,a,b):
        if b==0:
            print("Cannot divide by 0!")
        result = a/b
        self.history.append(f"{a} / {b} = {result}")
        return result
    