def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def division(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero!")
    return a / b


try:
    assert add(2, 3) == 5
    assert subtract(5, 2) == 3
    assert multiply(4, 3) == 12
    assert division(10, 2) == 5

    print("All tests passed!")

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    operation = input("Choose an operation (+, -, *, /): ")

    if operation == "+":
        print("Answer:", add(num1, num2))
    elif operation == "-":
        print("Answer:", subtract(num1, num2))
    elif operation == "*":
        print("Answer:", multiply(num1, num2))
    elif operation == "/":
        print("Answer:", division(num1, num2))
    else:
        print("Invalid operation!")

except ValueError:
    print("Please enter numerical values only!")

except ZeroDivisionError:
    print("ZeroDivisionError: You cannot divide by zero!")

except AssertionError:
    print("AssertionError: A test failed!")