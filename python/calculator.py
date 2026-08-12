"""
DevForge - Python Calculator Utility

A simple command-line calculator supporting
basic arithmetic operations.
"""


def calculator():
    print("=== DevForge Calculator ===")

    try:
        first = float(input("Enter first number: "))
        operator = input("Enter operation (+, -, *, /, **): ")
        second = float(input("Enter second number: "))

        if operator == "+":
            result = first + second
        elif operator == "-":
            result = first - second
        elif operator == "*":
            result = first * second
        elif operator == "/":
            if second == 0:
                print("Error: Cannot divide by zero.")
                return
            result = first / second
        elif operator == "**":
            result = first ** second
        else:
            print("Error: Invalid operator.")
            return

        print(f"Result: {result}")

    except ValueError:
        print("Error: Please enter valid numbers.")


if __name__ == "__main__":
    calculator()
