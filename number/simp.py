from enum import Enum

class MenuOption(Enum):
    ADD = 1
    SUBTRACT = 2
    EXIT = 3

def add_numbers(a, b):
    """Add two numbers and return the result."""
    return a + b

def subtract_numbers(a, b):
    """Subtract the second number from the first and return the result."""
    return a - b

def main():
    while True:
        # Display menu
        print("\nChoose an option:")
        print("1. Add two numbers")
        print("2. Subtract two numbers")
        print("3. Exit")

        # Get user choice
        try:
            choice = int(input("Enter the number of your choice: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        # Perform the chosen operation
        if choice == MenuOption.ADD.value:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = add_numbers(num1, num2)
            print(f"The sum of {num1} and {num2} is: {result}")
        elif choice == MenuOption.SUBTRACT.value:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = subtract_numbers(num1, num2)
            print(f"The difference of {num1} and {num2} is: {result}")
        elif choice == MenuOption.EXIT.value:
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid menu option.")

if __name__ == "__main__":
    main()
