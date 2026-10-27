
def Hello(name):
  
  print("Hello", name)

name = input("What is your name? ")
Hello(name)

def square(number):
  print(number * number)

number = int(input("Enter a number: "))
print("The square is", number * number)


def addition(first, second): print(first + second)
    

def subtraction(first, second): print(first - second)


def multiplication(first, second): print(first * second)



first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))

print("Addition:")
addition(first, second)

print("Subtraction:")
subtraction(first, second)

print("Multiplication:")
multiplication(first, second)