import math 

class AdvanceCalculator:
    def __init__(self):
        self.history = [] # To store all our calculations
        
    def addition(self,a,b):     # ADDITION
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result

    def subtraction(self,a,b):  # SUBTRACTION
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result

    def multiply(self,a,b):     # MULTIPLICATION
        result = a * b
        self.history.append(f"{a} x {b} = {result}")
        return result

    def division(self,a,b):     # DIVISION
        if b==0:
            return "Cannot divide by 0!"
        result = a/b
        self.history.append(f"{a} / {b} = {result:.3f}")
        return round(result,3) # Round off to 3

    def power(self,a,b):        # POWER
        result = a**b
        self.history.append(f"{a} ^ {b} = {result}")
        return result

    def squareroot(self,a):     # SQUAREROOT
        if a < 0:
            return "Cannot calculate square root of a negative number!"
        result = math.sqrt(a)
        self.history.append(f"sqrt({a}) = {result:.3f}") # Result will show upto 3 decimal places
        return round(result,3)      # Round off result to 3 decimal places
    
    def sin(self, angle_degrees):      # SIN FUNCTION
        radians = math.radians(angle_degrees)
        result = math.sin(radians)
        self.history.append(f"sin({angle_degrees}°) = {result:.3f}") # Result will show upto 3 decimal places
        return round(result, 3)     # Round off result to 3 decimal places
    
    def cos(self, angle_degrees):       # COS FUNCTION
        radians = math.radians(angle_degrees)
        result = math.cos(radians)
        self.history.append(f"cos({angle_degrees}°) = {result:.3f}") # Result will show upto 3 decimal places
        return round(result, 3)     # Round off result to 3 decimal places
    
    def tan(self, angle_degrees):       # TAN FUNCTION
        radians = math.radians(angle_degrees)
        result = math.tan(radians)
        self.history.append(f"tan({angle_degrees}°) = {result:.3f}") # Result will show upto 3 decimal places
        return round(result, 3)     # Round off result to 3 decimal places
    
    def quadratic_formula(self, a, b, c):   # QUADRATIC FORMULA FOR ROOTS
        if a == 0:
            return "Error: If 'a' is 0, it is not a quadratic equation!"
            
        discriminant = (b**2) - (4 * a * c)
        
        if discriminant < 0:
            return "Complex roots (discriminant is negative)."
            
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        
        self.history.append(f"Quadratic roots for {a}x^2 + {b}x + {c}: {root1:.2f}, {root2:.2f}")
        return root1, root2
    
    def showhistory(self):          # HISTORY OF ALL CALCULATIONS
        print()
        print("----- Calculation History -----")
        if not self.history:
            print("No calculations yet.")
        else:
            for item in self.history:
                print(item)
        print("----------------------")
    
    
    
        