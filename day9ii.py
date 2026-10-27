numbers = [13, 27, 36, 43, 25, 41, 17, 98, 9, 110]

total = sum(numbers)

for number in numbers:
    if number % 2 == 0:
        print(number, "is even")
    else:
        print(number, "is odd")

print("Total sum of numbers:", total)