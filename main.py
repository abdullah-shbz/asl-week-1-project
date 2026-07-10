from calculator import AdvanceCalculator

calc = AdvanceCalculator()
    
    # LOOP
while True:
    print("\n" + "="*30)
    print("ADVANCED CLI CALCULATOR")
    print("="*30)
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square Root")
    print("7. Sine (Trigonometry)")
    print("8. Cosine (Trigonometry)")
    print("9. Tangent (Trigonometry)")
    print("10. Quadratic Formula")
    print("11. Show History")
    print("0. Exit")
    print("="*30)
        
    choice = input("Select an option (0-11): ")
        
        # Non-math commands
    if choice == '0':
        print("Exiting calculator. Great job this week, bro!")
        break
    elif choice == '11':    # Calculation History
        calc.showhistory()
        continue
            
        
    try:        # Error Handling
        
        if choice in ['1', '2', '3', '4', '5']:     # Requires 2 inputs
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
                
            if choice == '1':   # Addition
                print(f"Result: {calc.addition(num1, num2)}")
            elif choice == '2': # Subtraction
                print(f"Result: {calc.subtraction(num1, num2)}")
            elif choice == '3': # Multiplication
                print(f"Result: {calc.multiply(num1, num2)}")
            elif choice == '4': # Division
                print(f"Result: {calc.division(num1, num2)}")
            elif choice == '5': # Power
                print(f"Result: {calc.power(num1, num2)}")
                
        elif choice == '6':     # Square Root
            num = float(input("Enter the number: "))
            print(f"Result: {calc.squareroot(num)}")
                
            # trignomatic functions
        elif choice in ['7', '8', '9']:
            angle = float(input("Enter the angle in degrees: "))
            if choice == '7': 
                print(f"Result: {calc.sin(angle)}")
            elif choice == '8': 
                print(f"Result: {calc.cos(angle)}")
            elif choice == '9': 
                print(f"Result: {calc.tan(angle)}")
                
        elif choice == '10':    # Quadratic Formula
            print("Equation format: ax^2 + bx + c = 0")
            a = float(input("Enter a: "))
            b = float(input("Enter b: "))
            c = float(input("Enter c: "))
            print(f"Result: {calc.quadratic_formula(a, b, c)}")
                
        else:
            print("Invalid choice. Please pick a valid number from the menu.")
                
    except ValueError:      # for inputs other than numbers
        print("Invalid input! Please enter numbers only.")

