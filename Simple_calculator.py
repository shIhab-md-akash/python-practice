def add(x, y):
    
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def modulus(x, y):
    if y == 0:
        return "Error! Modulus by zero."
    return x % y


# Main Program
def calculator():
    print("Simple Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")

    try:
        choice = int(input("Enter choice (1-5): "))
        if choice not in [1, 2, 3, 4, 5]:
            print("Invalid choice! Please select between 1 and 5.")
            return

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == 1:
            print("Result:", add(num1, num2))
        elif choice == 2:
            print("Result:", subtract(num1, num2))
        elif choice == 3:
            print("Result:", multiply(num1, num2))
        elif choice == 4:
            print("Result:", divide(num1, num2))
        elif choice == 5:
            print("Result:", modulus(num1, num2))

    except ValueError:
        print("Invalid input! Please enter numeric values only.")


# Run the calculator
if __name__ == "__main__":

    calculator()
