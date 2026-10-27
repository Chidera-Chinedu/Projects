
from calcii import add, subtract, multiply, division

# Test the calc functions oOR ELSE
print("Welcome to me calculator!")

try:
	first = float(input("Enter the first number: "))
	second = float(input("Enter the second number: "))
	print("addition:", add(first, second))
	print("subtraction:", subtract(first, second))
	print("multiplication:", multiply(first, second))
	print("division:", division(first, second))
except ValueError as error:
	print("Error:", error)

    
