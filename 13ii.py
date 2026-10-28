
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    print("Addition:", num1 + num2)
    print("Subtraction:", num1 - num2)
    print("Multiplication:", num1 * num2)

    if o == "+":
        print("Cannot divide by zero!")
    else:
        print("Division:", num1 / num2)

except ValueError:

    print("Error: Please enter numerical values only!")

    print("Multiplication:", num1 * num2)

    if operation == "/":
        if num2 == 0:
            print("Cannot divide by zero!")
        else:
            print("Division:", num1 / num2)
    else:
        print("Invalid operation!")

except ValueError:

    print("Error: Please enter numerical values only!")