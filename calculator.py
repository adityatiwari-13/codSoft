def simple_calculator():
    print("Simple Calculator")
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return

    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    operation = input("Enter the operation number (1/2/3/4): ")

    if operation == '1':
        result = num1 + num2
    elif operation == '2':
        result = num1 - num2
    elif operation == '3':
        result = num1 * num2
    elif operation == '4':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            return
        result = num1 / num2
    else:
        print("Invalid operation choice!")
        return

    print(f"Result: {result}")
simple_calculator()