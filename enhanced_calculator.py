# Enhanced Calculator with Extra Features

def calculator():
    while True:
        try:
            # Prompt user for two numbers
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            # Display available operations
            print("\nChoose an operation:")
            print("1. Addition (+)")
            print("2. Subtraction (-)")
            print("3. Multiplication (*)")
            print("4. Division (/)")
            print("5. Power (**) - Exponentiation")
            print("6. Modulus (%) - Remainder")

            # Prompt user for operation choice
            operation = input("\nEnter the operation (+, -, *, /, **, %): ")

            # Perform the calculation based on the operation
            if operation == '+':
                result = num1 + num2
                print(f"\n{num1} + {num2} = {result}")
            elif operation == '-':
                result = num1 - num2
                print(f"\n{num1} - {num2} = {result}")
            elif operation == '*':
                result = num1 * num2
                print(f"\n{num1} * {num2} = {result}")
            elif operation == '/':
                if num2 != 0:
                    result = num1 / num2
                    print(f"\n{num1} / {num2} = {result}")
                else:
                    print("\nError: Division by zero is not allowed.")
            elif operation == '**':
                result = num1 ** num2
                print(f"\n{num1} raised to the power of {num2} = {result}")
            elif operation == '%':
                result = num1 % num2
                print(f"\n{num1} % {num2} = {result}")
            else:
                print("\nInvalid operation! Please select a valid operator.")
        
        except ValueError:
            print("\nError: Please enter valid numeric inputs.")

        # Ask the user if they want to perform another calculation
        choice = input("\nWould you like to perform another calculation? (yes/no): ").strip().lower()
        if choice != 'yes':
            print("\nThank you for using the calculator. Goodbye!")
            break

# Run the enhanced calculator
calculator()

