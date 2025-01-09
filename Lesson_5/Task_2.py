def run_calculator():
    while True:
        try:
            a = float(input("Enter the first number: "))
            op = input("Enter the operator (+, -, *, /): ").strip()
            b = float(input("Enter the second number: "))
        except ValueError:
            print("Error: invalid input. Please try again.\n")
            continue

        if op == '+':
            result = a + b
        elif op == '-':
            result = a - b
        elif op == '*':
            result = a * b
        elif op == '/':
            if b == 0:
                print("Error: division by zero.\n")
                continue
            else:
                result = a / b
        else:
            print(f"Unknown operator: {op}\nPlease try again.\n")
            continue

        print(f"Result: {result}\n")

        answer = input("Continue? (y/yes, otherwise exit): ").lower().strip()
        if answer not in ('y', 'yes'):
            print("Calculator finished.")
            break

if __name__ == "__main__":
    run_calculator()