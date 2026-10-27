try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    operation = input("Choose an operation (+, -, *, /): ")

    if operation == "+":
        print("Answer:", num1 + num2)

    elif operation == "-":
        print("Answer:", num1 - num2)

    elif operation == "*":
        print("Answer:", num1 * num2)

    elif operation == "/":
        if num2 != 0:
            print("Answer:", num1 / num2)
        else:
            print("Error: Cannot divide by zero!")

    else:
        print("Invalid operation!")

except ValueError:
    print("Error: Please enter numerical values only!")