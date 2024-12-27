number_1 = float(input("Please enter a first number: "))
number_2 = float(input("Please enter a second number:"))

operation = input("Enter the operation (+, -, /, *): ")

if operation == '+':
    result = number_1 + number_2
elif operation == '-':
    result = number_1 - number_2
elif operation == '*':
    result = number_1 * number_2
elif operation == '/':
    if number_2 == 0:
        print("Error: Division by zero is not possible!")
        exit()
    else:
        result = number_1 / number_2
else:
    print("Unknown operation!")
    exit()

print("Result: ", result)